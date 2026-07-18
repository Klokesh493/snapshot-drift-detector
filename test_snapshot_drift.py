import unittest

from snapshot_drift import offenders


class SnapshotDriftTest(unittest.TestCase):
    def test_flags_large_schedule_drift(self):
        rows = [{"workload": "reports", "expected_interval_hours": "6", "actual_interval_hours": "14"}]
        self.assertEqual(offenders(rows), ["reports"])


if __name__ == "__main__":
    unittest.main()
