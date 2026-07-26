# Evidence-Driven Threat Intelligence & Attack Classification Engine

## Overview
The **Evidence-Driven Threat Intelligence & Attack Classification Engine** aggregates evidence from previous phases (Behaviour Profiles, Anomaly Scores, Context Assessments, Reasoning Traces) to rank multiple threat hypotheses, classify primary security threats, map MITRE ATT&CK tactics/techniques, and construct multi-stage attack chains.

## Key Modules
- `evidence_aggregator.py`: Aggregates multi-source evidence into a structured graph.
- `hypothesis_engine.py`: Generates & ranks probabilistic threat hypotheses.
- `threat_classifier.py`: Classifies primary attack category without using LLMs.
- `mitre_mapper.py`: Maps classified threats to MITRE ATT&CK framework IDs & tactics.
- `attack_chain_builder.py`: Constructs temporal multi-stage attack progression graphs.
- `threat_repository.py`: Manages PostgreSQL persistence & empirical evaluation metrics.
- `threat_engine.py`: High-level orchestrator & evaluation manager.
- `threat_api.py`: REST Endpoint Router for `/api/v1/threat/*`.
