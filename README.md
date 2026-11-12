# Snapshot Drift Detector

A snapshot schedule can drift gradually from its intended cadence, increasing the time between recovery points.

## What I built

I built a schedule audit that computes the absolute difference between intended and observed snapshot intervals. It flags workloads more than two hours outside the expected cadence.

## How it works

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

[Architecture](docs/ARCHITECTURE.md) · [Decision rules and source](docs/RULES.md)

## Tools used

| Tool | Role in this repository |
| --- | --- |
| Python | [snapshot_drift.py](snapshot_drift.py) implements the CLI and decision rules. Uses `csv` to read tabular exports. |
| Make | Runs the documented example and the local `unittest` suite. |
| Python replay runner | Compares actual stdout with the checked-in baseline fixtures. |
| Ruff and Bandit | Developer lint and static security checks through `make check`. |

## Run the project

Use Python 3.10+ and Make. From the repository root:

```sh
python3 snapshot_drift.py sample_snapshots.csv
```

The reports workload exceeds the tolerance and is printed for review. [Full expected output](examples/Demo%201.stdout.txt)

### Additional replay cases

- **Last sample record in isolation** · `python3 snapshot_drift.py examples/last-record.csv` · [Expected output](examples/Last%20sample%20record%20in%20isolation.stdout.txt)

## Verify the project

```sh
make verify
make replay
```

`make replay` checks the recorded cases and exits nonzero if the output changes.
See the [developer guide](docs/DEVELOPMENT.md) for the pinned lint and security tools.

## Operating limits

The tool works on intervals supplied in an export. Check backup completion and recoverability separately.

[Case study](docs/CASE_STUDY.md) · [Operator runbook](docs/RUNBOOK.md) · [Verification report](reports/verification.md)
