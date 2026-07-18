# Snapshot Drift Detector

Compares expected and actual snapshot schedules to catch policy drift.

Focus: Backup-platform DevSecOps governance.

Built as a small, runnable Python project with clear input, output, sample data, and tests.

## Run

```bash
python3 snapshot_drift.py sample_snapshots.csv
```

## Verify

```bash
python3 -m unittest discover . -v
```
