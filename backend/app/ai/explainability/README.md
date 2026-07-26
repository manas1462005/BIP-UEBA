# Explainability & Analyst Copilot Engine

## Overview
The **Explainability & Analyst Copilot Engine** converts deterministic outputs from previous phases (Behaviour Profiles, Hybrid Anomaly Scores, Context Assessments, Threat Classifications, MITRE Mappings, and Attack Chains) into **100% evidence-grounded human-readable investigations**, **Executive Summaries**, **Chronological Timelines**, **Actionable Recommendations**, and a **Conversational Analyst Copilot**.

## Key Modules
- `grounding_engine.py`: Bundles multi-phase outputs into a sealed Evidence Package.
- `prompt_builder.py`: System prompts enforcing strict evidence grounding rules.
- `citation_engine.py`: Attaches exact evidence citations to each generated sentence.
- `timeline_builder.py`: Constructs step-by-step chronological investigation timelines.
- `executive_summary.py`: Generates business-friendly executive summaries.
- `technical_summary.py`: Generates detailed technical analyst narratives.
- `recommendation_engine.py`: Maps evidence & MITRE tactics to SOC analyst action checklists.
- `copilot_engine.py`: Grounded conversational Q&A assistant for SOC analysts.
- `explanation_engine.py`: Orchestrator running grounding, timelines, summaries & copilot.
- `explainability_repository.py`: Persistence & empirical evaluation metrics repository.
- `explainability_api.py`: REST Endpoint Router for `/api/v1/explain/*`.
