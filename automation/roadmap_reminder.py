#!/usr/bin/env python3
"""Generate the daily roadmap plan, Telegram reminders, and progress dashboard."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "schedule" / "reminders.json"
SCHEDULE_PATH = ROOT / "schedule" / "52-weeks.md"
TODAY_PATH = ROOT / "TODAY.md"
PROGRESS_PATH = ROOT / "tracking" / "daily-progress.md"
LABEL = "roadmap-progress"


@dataclass(frozen=True)
class WeekPlan:
    number: int
    focus: str
    evidence: str
    stretch: str


def load_config() -> dict[str, Any]:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def parse_week_plans(text: str) -> dict[int, WeekPlan]:
    plans: dict[int, WeekPlan] = {}
    pattern = re.compile(
        r"^\|\s*(\d+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*$"
    )
    for line in text.splitlines():
        match = pattern.match(line)
        if match:
            number = int(match.group(1))
            plans[number] = WeekPlan(number, match.group(2), match.group(3), match.group(4))
    if len(plans) != 52:
        raise ValueError(f"Expected 52 roadmap weeks, found {len(plans)}")
    return plans


def roadmap_week(today: date, start: date) -> int:
    if today < start:
        return 0
    return ((today - start).days // 7) + 1


def phase_for_week(config: dict[str, Any], week: int) -> str:
    for phase in config["phases"]:
        if phase["start"] <= week <= phase["end"]:
            return str(phase["name"])
    return "Roadmap complete" if week > 52 else "Pre-roadmap setup"


def choose_period(now: datetime, config: dict[str, Any]) -> str:
    hour = now.hour
    if hour < 12:
        return "morning"
    if hour < 20:
        return "evening"
    return "night"


def github_api(
    method: str,
    path: str,
    token: str,
    payload: dict[str, Any] | None = None,
) -> Any:
    url = f"https://api.github.com{path}"
    body = json.dumps(payload).encode("utf-8") if payload is not None else None
    request = urllib.request.Request(url, data=body, method=method)
    request.add_header("Accept", "application/vnd.github+json")
    request.add_header("Authorization", f"Bearer {token}")
    request.add_header("X-GitHub-Api-Version", "2022-11-28")
    if body is not None:
        request.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(request, timeout=30) as response:
        data = response.read()
    return json.loads(data) if data else None


def issue_title(plan: WeekPlan) -> str:
    return f"[Roadmap] Week {plan.number:02d} — {plan.focus}"


def issue_body(plan: WeekPlan, phase: str) -> str:
    return f"""## Week {plan.number}: {plan.focus}

**Phase:** {phase}<br>
**Required evidence:** {plan.evidence}

Check each block after completing it:

- [ ] Monday — plan the week and reserve study time
- [ ] Tuesday — concepts and derivations (90 min)
- [ ] Wednesday — guided implementation (90 min)
- [ ] Thursday — independent implementation (90 min)
- [ ] Friday — recovery or oral review (30 min)
- [ ] Saturday — project and controlled experiment (3 hours)
- [ ] Sunday — project, writing, interview rehearsal, and weekly review (2.5 hours)
- [ ] Required evidence committed or linked in this issue

## Weekly reflection

- Hours completed:
- What I learned:
- Largest blocker:
- Adjustment for next week:

Close this issue after the required evidence is complete. The progress dashboard updates whenever this issue is edited or closed.
"""


def ensure_weekly_issue(repo: str, token: str, plan: WeekPlan, phase: str) -> str:
    query = urllib.parse.urlencode(
        {"labels": LABEL, "state": "all", "per_page": "100", "sort": "created"}
    )
    issues = github_api("GET", f"/repos/{repo}/issues?{query}", token)
    title = issue_title(plan)
    for issue in issues:
        if "pull_request" not in issue and issue.get("title") == title:
            return str(issue["html_url"])

    try:
        github_api(
            "POST",
            f"/repos/{repo}/labels",
            token,
            {"name": LABEL, "color": "1f883d", "description": "AI roadmap weekly progress"},
        )
    except urllib.error.HTTPError as error:
        if error.code != 422:  # Label already exists.
            raise

    issue = github_api(
        "POST",
        f"/repos/{repo}/issues",
        token,
        {"title": title, "body": issue_body(plan, phase), "labels": [LABEL]},
    )
    return str(issue["html_url"])


def today_markdown(
    today: date,
    plan: WeekPlan,
    phase: str,
    session: dict[str, Any],
    issue_url: str,
    config: dict[str, Any],
) -> str:
    reminders = config["reminders"]
    issue_line = f"[Open this week's check-in]({issue_url})" if issue_url else "The weekly check-in is created by the reminder workflow."
    return f"""# Today’s Roadmap

**Date:** {today.strftime('%A, %B %-d, %Y')}<br>
**Week:** {plan.number} of 52<br>
**Phase:** {phase}<br>
**Weekly focus:** {plan.focus}

## Today’s session

**Time:** {session['minutes']} minutes<br>
**Task:** {session['work']}

## Required evidence this week

{plan.evidence}

## Check in

{issue_line}

## Daily reminders

- Morning: {reminders['morning']} Pacific
- Evening: {reminders['evening']} Pacific
- Night: {reminders['night']} Pacific

This page is generated from [`schedule/52-weeks.md`](schedule/52-weeks.md) and [`schedule/reminders.json`](schedule/reminders.json). Do not edit it manually.
"""


def reminder_message(
    period: str,
    today: date,
    plan: WeekPlan,
    phase: str,
    session: dict[str, Any],
    issue_url: str,
    repo: str,
) -> str:
    today_url = f"https://github.com/{repo}/blob/main/TODAY.md"
    header = {
        "morning": "☀️ Morning roadmap plan",
        "evening": "🚀 Evening study reminder",
        "night": "🌙 Nightly roadmap check-in",
    }[period]
    prompts = {
        "morning": "Read the goal, reserve the time, and define the smallest first action.",
        "evening": "Start with just 10 focused minutes. Momentum can do the rest.",
        "night": "Tick what you completed. Partial progress counts; record the blocker honestly.",
    }
    progress = f"\nCheck in: {issue_url}" if issue_url else ""
    return (
        f"{header}\n\n"
        f"{today.strftime('%A, %B %-d')} · Week {plan.number}/52\n"
        f"Phase: {phase}\n"
        f"Focus: {plan.focus}\n\n"
        f"Today ({session['minutes']} min): {session['work']}\n\n"
        f"Evidence: {plan.evidence}\n\n"
        f"{prompts[period]}\n"
        f"Today’s page: {today_url}{progress}"
    )


def send_telegram(token: str, chat_id: str, message: str) -> None:
    endpoint = f"https://api.telegram.org/bot{token}/sendMessage"
    body = urllib.parse.urlencode(
        {"chat_id": chat_id, "text": message, "disable_web_page_preview": "true"}
    ).encode("utf-8")
    request = urllib.request.Request(endpoint, data=body, method="POST")
    with urllib.request.urlopen(request, timeout=30) as response:
        result = json.loads(response.read())
    if not result.get("ok"):
        raise RuntimeError("Telegram rejected the reminder")


def checkbox_counts(body: str) -> tuple[int, int]:
    boxes = re.findall(r"^- \[([ xX])\] ", body or "", flags=re.MULTILINE)
    return sum(value.lower() == "x" for value in boxes), len(boxes)


def sync_progress(repo: str, token: str) -> None:
    query = urllib.parse.urlencode({"labels": LABEL, "state": "all", "per_page": "100"})
    issues = github_api("GET", f"/repos/{repo}/issues?{query}", token)
    rows: list[tuple[int, str]] = []
    completed_total = 0
    task_total = 0
    latest_update = ""
    for issue in issues:
        if "pull_request" in issue:
            continue
        match = re.search(r"\[Roadmap\] Week (\d+)", issue.get("title", ""))
        if not match:
            continue
        week = int(match.group(1))
        completed, total = checkbox_counts(issue.get("body", ""))
        completed_total += completed
        task_total += total
        latest_update = max(latest_update, issue.get("updated_at", ""))
        percent = round((completed / total) * 100) if total else 0
        state = "Complete" if issue.get("state") == "closed" else "In progress"
        focus = re.sub(r"^\[Roadmap\] Week \d+ — ", "", issue["title"])
        link = f"[Week {week}]({issue['html_url']})"
        rows.append((week, f"| {link} | {focus} | {completed}/{total} | {percent}% | {state} |"))

    rows.sort(key=lambda item: item[0])
    overall = round((completed_total / task_total) * 100) if task_total else 0
    table = "\n".join(row for _, row in rows) or "| — | No weekly check-in created yet | 0/0 | 0% | Not started |"
    if latest_update:
        synchronized = datetime.fromisoformat(latest_update.replace("Z", "+00:00")).astimezone(
            ZoneInfo("America/Los_Angeles")
        )
    else:
        synchronized = datetime.now(ZoneInfo("America/Los_Angeles"))
    content = f"""# Daily Progress

Automatically generated from GitHub issues labeled `{LABEL}`.

**Last activity:** {synchronized.strftime('%Y-%m-%d %H:%M Pacific')}<br>
**Overall checklist completion:** {completed_total}/{task_total} ({overall}%)

| Week | Focus | Completed | Progress | Status |
|---|---|---:|---:|---|
{table}

## How to update progress

Open the current week, tick completed checkboxes, add the weekly reflection, and close the issue only after committing the required evidence. This dashboard will update automatically.
"""
    PROGRESS_PATH.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--period", choices=["auto", "morning", "evening", "night"], default="auto")
    parser.add_argument("--date", help="Override local date (YYYY-MM-DD), useful for tests")
    parser.add_argument("--send", action="store_true", help="Send the Telegram notification")
    parser.add_argument("--ensure-issue", action="store_true", help="Create/find this week's check-in")
    parser.add_argument("--write-today", action="store_true", help="Generate TODAY.md")
    parser.add_argument("--sync-progress", action="store_true", help="Regenerate tracking/daily-progress.md")
    args = parser.parse_args()

    config = load_config()
    timezone = ZoneInfo(config["timezone"])
    now = datetime.now(timezone)
    today = date.fromisoformat(args.date) if args.date else now.date()
    start = date.fromisoformat(config["start_date"])
    week = roadmap_week(today, start)
    if not 1 <= week <= 52:
        print(f"No active roadmap week for {today} (calculated week: {week}).")
        return 0

    plans = parse_week_plans(SCHEDULE_PATH.read_text(encoding="utf-8"))
    plan = plans[week]
    phase = phase_for_week(config, week)
    session = config["cadence"][today.strftime("%A")]
    period = choose_period(now, config) if args.period == "auto" else args.period
    repo = os.environ.get("GITHUB_REPOSITORY", "samratdotm/ai-research-engineer-roadmap")
    github_token = os.environ.get("GITHUB_TOKEN", "")
    issue_url = ""

    if args.ensure_issue:
        if not github_token:
            raise RuntimeError("GITHUB_TOKEN is required for --ensure-issue")
        issue_url = ensure_weekly_issue(repo, github_token, plan, phase)

    if args.write_today:
        TODAY_PATH.write_text(
            today_markdown(today, plan, phase, session, issue_url, config), encoding="utf-8"
        )

    if args.sync_progress:
        if not github_token:
            raise RuntimeError("GITHUB_TOKEN is required for --sync-progress")
        sync_progress(repo, github_token)

    message = reminder_message(period, today, plan, phase, session, issue_url, repo)
    if args.send:
        telegram_token = os.environ.get("TELEGRAM_BOT_TOKEN", "")
        telegram_chat_id = os.environ.get("TELEGRAM_CHAT_ID", "")
        if not telegram_token or not telegram_chat_id:
            raise RuntimeError("TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID are required for --send")
        send_telegram(telegram_token, telegram_chat_id, message)
        print(f"Sent {period} reminder for roadmap week {week}.")
    else:
        print(message)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, ValueError, urllib.error.URLError) as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1)
