# AI & Behavioral Intelligence Architecture Subsystem

This package defines the modular AI/ML pipeline for the Behavioral Intelligence Platform.

## Module Structure & Future Responsibilities

- **`anomaly/`**: Unsupervised anomaly detection models (Isolation Forest, Autoencoders, DBSCAN, Sequence Anomaly Detection).
- **`profiling/`**: Baseline profile calculation, statistical distribution tracking, and behavioral vector representation.
- **`reasoning/`**: Contextual risk reasoning engine, risk graph evaluation, and temporal window correlation.
- **`classification/`**: Threat tactic classification, MITRE ATT&CK mapping, and alert prioritization.
- **`explainability/`**: Explainable AI (XAI) features using SHAP, LIME, and natural language rationale generation.
- **`synthetic/`**: Telemetry event generation and attack sequence simulation for model evaluation.
