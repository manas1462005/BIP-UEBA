from fastapi import APIRouter
from app.api.v1.endpoints import health, auth, simulator, enterprise
from app.ai.profiling.profile_api import router as profiling_router
from app.ai.anomaly.anomaly_api import router as anomaly_router
from app.ai.context.context_api import router as context_router
from app.ai.threat.threat_api import router as threat_router
from app.ai.explainability.explainability_api import router as explainability_router
from app.pipeline.pipeline_api import router as pipeline_router

api_router = APIRouter()

api_router.include_router(health.router, tags=["Health"])
api_router.include_router(auth.router, tags=["Authentication"])
api_router.include_router(simulator.router, tags=["Telemetry Simulator"])
api_router.include_router(enterprise.router, tags=["Enterprise Context Layer"])
api_router.include_router(profiling_router, prefix="/profiles", tags=["Behaviour Intelligence Profiling"])
api_router.include_router(anomaly_router, prefix="/anomaly", tags=["Hybrid Anomaly Intelligence Engine"])
api_router.include_router(context_router, prefix="/context", tags=["Context Intelligence & Reasoning Engine"])
api_router.include_router(threat_router, prefix="/threat", tags=["Evidence-Driven Threat Intelligence Engine"])
api_router.include_router(explainability_router, prefix="/explain", tags=["Explainability & Analyst Copilot Engine"])
api_router.include_router(pipeline_router, prefix="/pipeline", tags=["End-to-End AI Event Processing Pipeline"])
