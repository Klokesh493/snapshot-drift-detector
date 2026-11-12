# Snapshot Drift Detector walkthrough

## Business problem

A snapshot schedule can drift gradually from its intended cadence, increasing the time between recovery points.

## Reproduce the workflow

Run `python3 snapshot_drift.py sample_snapshots.csv` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
reports
```

The sample supplies these fields. `workload`, `expected_interval_hours`, `actual_interval_hours`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
