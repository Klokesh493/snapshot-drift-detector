# Snapshot Drift Detector architecture

Compares expected and actual snapshot schedules to catch policy drift.

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

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
