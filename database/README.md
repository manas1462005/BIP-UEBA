# Database Schema & Migrations

This directory hosts database initialization scripts, schemas, and database configuration context for PostgreSQL and Alembic.

## Schema Overview (Phase 1)
- `users`: User identity & authentication
- `roles`: Role definitions (Admin, Analyst, Viewer)
- `organizations`: Multi-tenant organization structure
- `devices`: Managed endpoints & assets
- `behaviour_profiles`: Base behavioral baseline containers
- `sessions`: User login sessions
- `events`: Ingested security event telemetry log entries
- `alerts`: Behavioral anomaly alert containers
- `risk_scores`: Entity risk score tracking
- `attack_types`: Attack classification definitions
- `audit_logs`: Governance and access audit log trail

## Running Migrations Locally
Run Alembic migrations from `backend/`:
```bash
cd backend
alembic upgrade head
```
