# Behavioral Intelligence Platform (UEBA)

Enterprise-grade Context-Aware Behavioral Intelligence Platform (UEBA) designed for real-time security analytics, entity behavioral profiling, anomaly detection, attack classification, and explainable AI.

> **Phase 1 Status**: Monorepo Foundation & Core Architecture Complete.

---

## 🌟 Key Features (Phase 1 Foundation)

- **Clean Monorepo Architecture**: Clean separation between frontend React application, FastAPI backend, database migrations, documentation, and Docker orchestration.
- **FastAPI Core Architecture**: Built with Python 3.12, Pydantic v2, SQLAlchemy 2.0 ORM, and dependency injection.
- **Modern SOC Dashboard Shell**: React 18/19, TypeScript, Tailwind CSS, Lucide icons, Zustand state management, and protected routes.
- **PostgreSQL Data Models**: Unified ORM schema mapping Users, Roles, Organizations, Devices, BehaviourProfiles, Sessions, Events, Alerts, RiskScores, AttackTypes, and AuditLogs with explicit relationships.
- **JWT & Role Authentication Primitives**: RBAC structure (`Admin`, `Analyst`, `Viewer`), password hashing with Passlib/Bcrypt, and Axios authorization interceptors.
- **Docker Containerization**: Multi-stage Dockerfiles and `docker-compose.yml` for unified multi-container local stack launching.

---

## 🏗 System Architecture

```
Behavioral-Intelligence-Platform/
├── .github/
│   └── workflows/
│       └── ci.yml              # CI workflow for backend & frontend linting
├── backend/                    # Enterprise FastAPI Application
│   ├── alembic/                # Alembic database migration scripts
│   ├── app/
│   │   ├── api/v1/             # OpenAPI v1 endpoints & router aggregator
│   │   ├── core/               # Pydantic settings, logging, security primitives
│   │   ├── database/           # SQLAlchemy engine & session factory
│   │   ├── models/             # ORM entities (Users, Devices, Alerts, etc.)
│   │   ├── repositories/       # Generic BaseRepository pattern
│   │   ├── schemas/            # Pydantic validation schemas
│   │   ├── security/           # JWT & role-based dependencies
│   │   └── services/           # Business service layer abstractions
│   ├── main.py                 # FastAPI application factory & lifespan
│   └── requirements.txt
├── frontend/                   # SOC Console React Dashboard
│   ├── src/
│   │   ├── api/                # Axios client & request/response interceptors
│   │   ├── components/         # SOC Layout (Sidebar, Navbar, UserMenu, Breadcrumb)
│   │   ├── pages/              # Placeholder SOC pages (Dashboard, Users, Alerts...)
│   │   ├── store/              # Zustand Auth & UI state management
│   │   ├── styles/             # Tailwind CSS SOC Dark Theme definitions
│   │   └── types/              # Strict TypeScript interfaces
│   └── package.json
├── database/                   # DB setup SQL scripts
├── docker/                     # Dockerfiles for frontend and backend
├── docs/                       # Architecture and API documentation
├── scripts/                    # Development setup and utility scripts
├── docker-compose.yml          # Multi-service container launcher
├── LICENSE                     # MIT License
└── README.md                   # Platform documentation
```

---

## 💻 Tech Stack

| Layer | Technologies |
| :--- | :--- |
| **Frontend** | React 18/19, TypeScript, Vite, Tailwind CSS, Zustand, Axios, React Router v6, Lucide Icons |
| **Backend** | Python 3.12, FastAPI, Pydantic v2, SQLAlchemy 2.0, Alembic, Passlib (Bcrypt), Python-Jose |
| **Database** | PostgreSQL 16 (SQLite fallback for quick local execution) |
| **DevOps** | Docker, Docker Compose, GitHub Actions |

---

## 🚀 Running Locally

### Prerequisites
- **Python 3.12+**
- **Node.js 20+**
- **Docker Desktop** (Optional for container execution)

---

### 1. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run Alembic migrations
alembic upgrade head

# Launch Uvicorn dev server
uvicorn app.main:app --reload --port 8000
```

Backend will be live at:
- **API Base**: `http://localhost:8000/api/v1`
- **Health Check**: `http://localhost:8000/health`
- **Swagger Docs**: `http://localhost:8000/api/v1/docs`

---

### 2. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Run Vite dev server
npm run dev
```

Frontend SOC Console will be live at: `http://localhost:5173`

---

### 3. Quick Mock Login Credentials

| Role | Email | Password |
| :--- | :--- | :--- |
| **Admin** | `admin@bip.com` | `Admin123!` |
| **Analyst** | `analyst@bip.com` | `Analyst123!` |
| **Viewer** | `viewer@bip.com` | `Viewer123!` |

---

## 🐳 Docker Setup

Launch full stack (PostgreSQL + Backend + Frontend):

```bash
docker-compose up --build
```

Services started:
- **Frontend App**: `http://localhost:3000`
- **Backend FastAPI**: `http://localhost:8000`
- **PostgreSQL**: `localhost:5432`

---

## 🗺 Future Roadmap

- **Phase 2**: Event Ingestion Pipeline & Raw Telemetry Storage
- **Phase 3**: Statistical Baseline Profiling & Entity Feature Extraction
- **Phase 4**: Anomaly Detection & ML Model Integration
- **Phase 5**: MITRE ATT&CK Classification & Explainable AI (XAI)
- **Phase 6**: Real-Time Alerting, SIEM Integration, & Response Orchestration

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
