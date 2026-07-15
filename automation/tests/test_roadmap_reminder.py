import sys
import unittest
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo


sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import roadmap_reminder as reminder


class RoadmapReminderTests(unittest.TestCase):
    def test_schedule_contains_all_52_weeks(self):
        plans = reminder.parse_week_plans(reminder.SCHEDULE_PATH.read_text(encoding="utf-8"))
        self.assertEqual(len(plans), 52)
        self.assertEqual(plans[1].focus, "Vocabulary, lifecycle, baseline assessment")
        self.assertEqual(plans[52].number, 52)

    def test_week_boundaries(self):
        start = date(2026, 7, 13)
        self.assertEqual(reminder.roadmap_week(date(2026, 7, 12), start), 0)
        self.assertEqual(reminder.roadmap_week(start, start), 1)
        self.assertEqual(reminder.roadmap_week(date(2026, 7, 19), start), 1)
        self.assertEqual(reminder.roadmap_week(date(2026, 7, 20), start), 2)
        self.assertEqual(reminder.roadmap_week(date(2027, 7, 11), start), 52)

    def test_period_selection(self):
        config = reminder.load_config()
        zone = ZoneInfo(config["timezone"])
        self.assertEqual(reminder.choose_period(datetime(2026, 7, 15, 7, tzinfo=zone), config), "morning")
        self.assertEqual(reminder.choose_period(datetime(2026, 7, 15, 18, tzinfo=zone), config), "evening")
        self.assertEqual(reminder.choose_period(datetime(2026, 7, 15, 21, tzinfo=zone), config), "night")

    def test_checkbox_counts(self):
        body = "- [x] done\n- [ ] pending\n- [X] also done\n"
        self.assertEqual(reminder.checkbox_counts(body), (2, 3))


if __name__ == "__main__":
    unittest.main()
