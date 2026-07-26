# Adaptive Hierarchical Behaviour Intelligence Engine

## Overview
The **Adaptive Hierarchical Behaviour Intelligence Engine** continuously learns, aggregates, and versions behavioral baselines across 9 organizational levels:
1. **Enterprise**
2. **Business Unit**
3. **Department**
4. **Team**
5. **Project**
6. **Role**
7. **User**
8. **Device**
9. **Session**

## Module Structure

- `feature_extractor.py`: Extracts 30+ temporal, contextual, security, resource, relational, and network features from telemetry.
- `statistics_engine.py`: Computes rolling averages, moving windows, variances, and frequencies.
- `baseline_engine.py`: Synthesizes baseline working hours, IP subnets, and application distributions.
- `peer_group_engine.py`: Computes peer group statistics (Role peers, Team peers, Project peers, Regional peers).
- `seasonality_engine.py`: Isolates recurring calendar patterns (Release Weekends, Month-End, Public Holidays, On-call).
- `confidence_engine.py`: Computes baseline confidence score `[0.0, 1.0]` based on history length and stability.
- `maturity_engine.py`: Tracks profile maturity transitions (`New` → `Learning` → `Growing` → `Stable` → `Trusted` → `Archived`).
- `version_manager.py`: Manages profile snapshot versions (`v1`, `v2`, `v3`) with zero overwrite policy.
- `profile_builder.py`: Synthesizes complete hierarchical profiles & non-ML Behavior Fingerprints.
- `profile_repository.py`: Interface for PostgreSQL persistence.
- `profile_serializer.py`: Pydantic/JSON serialization tools.
- `profile_manager.py`: High-level orchestrator & dependency injection container.
- `profile_api.py`: FastAPI router for `/api/v1/profiles/*` endpoints.
