# Roadmap Reminder Setup

The repository can send three private Telegram reminders every day, maintain [`TODAY.md`](TODAY.md), create one progress issue per week, and turn its checkboxes into [`tracking/daily-progress.md`](tracking/daily-progress.md).

## 1. Create a Telegram bot

1. Open Telegram and start a chat with [`@BotFather`](https://t.me/BotFather).
2. Send `/newbot` and follow the prompts.
3. Copy the bot token. Treat it like a password; never commit it to this repository.
4. Open the new bot and press **Start**, or send it `/start`.

## 2. Find your Telegram chat ID

After sending `/start` to the bot, open this address in a browser, replacing `<TOKEN>` with the bot token:

```text
https://api.telegram.org/bot<TOKEN>/getUpdates
```

Find `message.chat.id` in the response and copy its numeric value. If `result` is empty, send the bot another message and reload the address.

## 3. Add GitHub Actions secrets

In this repository, open **Settings → Secrets and variables → Actions → New repository secret** and add:

| Secret | Value |
|---|---|
| `TELEGRAM_BOT_TOKEN` | Token from BotFather |
| `TELEGRAM_CHAT_ID` | Numeric chat ID from `getUpdates` |

## 4. Allow the workflow to update progress

Open **Settings → Actions → General → Workflow permissions**, choose **Read and write permissions**, and save.

The workflow also declares narrow `contents` and `issues` permissions in its YAML file.

## 5. Test before waiting for the schedule

1. Open **Actions → Daily roadmap reminders → Run workflow**.
2. Select `morning`.
3. Keep **Send the Telegram message** enabled.
4. Run the workflow.
5. Confirm that Telegram receives the message and that a weekly issue is created.

## Daily schedule

The schedule uses `America/Los_Angeles`, so daylight-saving changes are handled automatically.

| Reminder | Time | Purpose |
|---|---:|---|
| Morning | 7:15 AM | Show the week, topic, evidence, and today's task |
| Evening | 6:15 PM | Prompt the focused study session |
| Night | 9:15 PM | Link to the weekly progress check-in |

Edit [`schedule/reminders.json`](schedule/reminders.json) and the cron entries in [`.github/workflows/daily-reminders.yml`](.github/workflows/daily-reminders.yml) together if the times need to change.

## Recording progress

Each week, the automation creates an issue labeled `roadmap-progress`. Tick the session checkboxes as you work, write the short weekly reflection, and close the issue after the required evidence is committed. Editing or closing the issue regenerates the progress dashboard.

## Troubleshooting

- **No Telegram message:** Make sure you pressed **Start** in the bot chat and both secret names match exactly.
- **No scheduled runs:** Scheduled workflows must exist on the default branch and Actions must be enabled.
- **Dashboard does not commit:** Confirm **Read and write permissions** under the repository's Actions settings.
- **A reminder is a few minutes late:** GitHub-hosted scheduled jobs can be delayed during busy periods. The schedule uses minute 15 to avoid the busiest start-of-hour window.
