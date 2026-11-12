# Snapshot Drift Detector architecture

Compares expected and actual snapshot schedules to catch policy drift.

```mermaid
flowchart LR
    N0["sample_snapshots.csv"]
    N1["snapshot_drift.py"]
    N2["drift / offenders"]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
