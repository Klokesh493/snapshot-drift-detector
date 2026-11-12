# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 snapshot_drift.py sample_snapshots.csv
reports
test_flags_large_schedule_drift (test_snapshot_drift.SnapshotDriftTest) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
````
