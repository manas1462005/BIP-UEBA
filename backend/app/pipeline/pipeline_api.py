from typing import Dict, Any
from fastapi import APIRouter, Depends, status, Body
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.pipeline.pipeline_repository import PipelineRepository
from app.pipeline.pipeline_manager import PipelineManager
from app.pipeline.event_pipeline import EventPipeline

router = APIRouter()


@router.get("/status", status_code=status.HTTP_200_OK, summary="Get Pipeline Status & Stage Latencies")
def get_pipeline_status():
    return PipelineRepository.get_metrics()


@router.get("/metrics", status_code=status.HTTP_200_OK, summary="Get Empirical Pipeline Performance Metrics")
def get_pipeline_metrics():
    return PipelineRepository.get_metrics()


@router.post("/process", status_code=status.HTTP_200_OK, summary="Process Single Telemetry Event Through Full AI Pipeline")
def process_single_event(
    event: Dict[str, Any] = Body(
        default={
            "event_id": "evt_sim_30419",
            "entity_id": "alex.smith1@bip.com",
            "login_hour": 3,
            "session_duration_minutes": 15,
            "resource_accessed": "AWS Production Console",
            "vpn_used": False,
            "mfa_verified": False,
            "threat_label": "Credential Stuffing"
        }
    ),
    db: Session = Depends(get_db)
):
    pipeline = EventPipeline(db)
    return pipeline.process_event(event)
