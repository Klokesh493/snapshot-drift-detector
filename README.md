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

## Local verification

Run `make verify` with Make and Python 3 installed. The target runs the documented sample through the project CLI. It also runs the existing Python unit tests.

## Project walkthrough

```mermaid
flowchart LR
    A["Expected and actual snapshot intervals"]
    B["Compute absolute interval difference"]
    C{"Drift exceeds two hours?"}
    D["Emit affected workload"]
    E["Omit in-tolerance workload"]
    A --> B --> C
    C -->|Yes| D
    C -->|No| E
```

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)
