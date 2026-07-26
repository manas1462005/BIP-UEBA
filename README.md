# Behavioral Intelligence Platform (UEBA)

Enterprise-grade Context-Aware Behavioral Intelligence Platform (UEBA) designed for real-time security analytics, entity behavioral profiling, anomaly detection, attack classification, explainable AI, and judge-friendly assignment evaluation workflows.

> **Status**: Full Assignment Architecture, End-to-End AI Orchestration Pipeline, & Judge-Friendly Evaluation UI Complete.

---

## 🌟 Key Features

- **Synthetic Data Generator (Digital Twin)**: Generates 365-day enterprise digital twin security telemetry with 11 schema fields (`entity_id`, `entity_type`, `timestamp`, `source_ip`, `geo_location`, `resource_accessed`, `auth_method`, `session_duration`, `command_sequence`, `device_fingerprint`, `label`) across 8 attack scenarios.
- **Behavioural Baseline Profiling**: Learns non-ML statistical baseline normal behavior profiles per entity across 9 hierarchical levels without malicious classification.
- **Sequence-Aware Anomaly Detection**: Multi-detector ensemble combining Modified Z-Score, Isolation Forest, Peer Group Cohort Distance, Markov Chain Sequence Analysis, and Concept Drift Models.
- **Attack Classification & MITRE ATT&CK Mapping**: Classifies anomalies into 8 exact assignment attack categories (`Normal Baseline`, `Brute Force`, `Impossible Travel`, `Credential Stuffing`, `Lateral Movement`, `Device Spoofing`, `Low-and-Slow Exfiltration`, `Insider Drift`).
- **Grounded Explainability & Copilot Layer**: Generates 100% evidence-grounded executive summaries, cited technical narratives, chronological timelines, actionable recommendations, interactive Copilot Q&A, and downloadable 6-section investigation reports (`GET /api/v1/explain/report/full`).
- **Analyst SOC Workspace & Live Feed**: Enterprise SOC triage workspace with live incident feeds, node-link evidence graph visualizer, chronological timelines, and triage checklists.
- **End-to-End AI Event Processing Pipeline**: Single-event continuous orchestration (`backend/app/pipeline/`) with sub-2ms per-stage latency and real-time processing diagnostics (`/pipeline-monitor`).
- **Judge-Friendly Evaluator Workflow**: Reorganized 3-section sidebar (`Assignment Workflow`, `Investigation Workflow`, `Platform`), top horizontal pipeline ribbon, evaluation matrix, and quick demo sequence buttons (`Generate Synthetic Dataset`, `Run Detection Pipeline`, `View Explainability`, `Generate Final Report`).

---

## 🏗 System Architecture

```
Behavioral-Intelligence-Platform/
├── backend/                    # Enterprise FastAPI Application
│   ├── alembic/                # Database migration scripts
│   ├── app/
│   │   ├── ai/                 # AI Engines Subpackage
│   │   │   ├── profiling/      # Phase 3 Behaviour Profiling
│   │   │   ├── anomaly/        # Phase 4 Hybrid Anomaly Detection
│   │   │   ├── context/        # Phase 5 Context Reasoning Engine
│   │   │   ├── threat/         # Phase 6 Threat Classification & MITRE
│   │   │   └── explainability/ # Phase 7 Explainability & Report Generator
│   │   ├── pipeline/           # Phase 8.5 End-to-End Orchestration Pipeline
│   │   ├── simulator/          # Phase 2 Enterprise Telemetry Simulator
│   │   ├── api/v1/             # OpenAPI v1 router aggregator
│   │   ├── core/               # App configuration & security primitives
│   │   ├── database/           # SQLAlchemy engine & session factory
│   │   ├── models/             # ORM entities (Users, Events, Alerts, etc.)
│   │   └── tests/              # Backend unit & compliance test suite
│   ├── main.py                 # FastAPI application entrypoint
│   └── requirements.txt
├── frontend/                   # SOC Console React Application
│   ├── src/
│   │   ├── components/         # Layout (Sidebar, PipelineRibbon, AssignmentHeader)
│   │   ├── pages/              # Deliverable pages (AssignmentOverviewPage, etc.)
│   │   ├── api/                # Axios API client
│   │   └── styles/             # Tailwind CSS Dark Theme definitions
│   └── package.json
├── database/                   # DB schema SQL scripts
├── docker/                     # Container configuration
├── docs/                       # Architecture & compliance specifications
├── docker-compose.yml          # Multi-container local stack launcher
├── LICENSE                     # MIT License
└── README.md                   # Platform documentation
```

---

## 💻 Tech Stack

| Layer | Technologies |
| :--- | :--- |
| **Frontend** | React 18/19, TypeScript, Vite, Tailwind CSS, Zustand, Axios, React Router v6, Lucide Icons |
| **Backend** | Python 3.12, FastAPI, Pydantic v2, SQLAlchemy 2.0, Alembic, Scikit-Learn |
| **Database** | PostgreSQL 16 (SQLite fallback for quick local execution) |
| **DevOps** | Docker, Docker Compose, GitHub Actions |

---

## 🚀 Running Locally

### 1. Backend Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Backend endpoints:
- **API Base**: `http://localhost:8000/api/v1`
- **Swagger Docs**: `http://localhost:8000/docs`

### 2. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend SOC Console will be live at: `http://localhost:5173`

---

## 🧪 Running Automated Unit Tests

```bash
cd backend
python -m unittest discover -s app/tests -p "test_*.py"
```

All **75 unit tests** pass with 100% OK.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
