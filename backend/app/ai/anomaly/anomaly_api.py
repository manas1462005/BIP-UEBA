from typing import Dict, Any, List
from fastapi import APIRouter, Depends, status, Body
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.ai.anomaly.hybrid_engine import HybridEngine
from app.ai.anomaly.anomaly_repository import AnomalyRepository
from app.ai.profiling.profile_manager import ProfileManager

router = APIRouter()
engine = HybridEngine()


@router.post("/score", status_code=status.HTTP_200_OK, summary="Score Event Anomaly Across Detector Ensemble")
def score_event(
    event: Dict[str, Any] = Body(
        default={
            "event_id": "evt_sim_991",
            "entity_id": "alex.smith1@bip.com",
            "login_hour": 3,
            "session_duration_minutes": 120,
            "resource_accessed": "AWS Production Console",
            "vpn_used": False,
            "mfa_verified": False,
            "threat_label": "Credential Stuffing"
        }
    ),
    db: Session = Depends(get_db)
):
    entity_id = event.get("entity_id", "alex.smith1@bip.com")
    profile = ProfileManager(db).get_or_create_profile(entity_id, "user")
    result = engine.evaluate_event(event, profile)
    AnomalyRepository.log_inference(result)
    return result


@router.post("/train", status_code=status.HTTP_200_OK, summary="Train Ensemble Anomaly Models")
def train_anomaly_models(training_data: List[Dict[str, Any]] = Body(default=[])):
    return engine.train_models(training_data)


@router.post("/retrain", status_code=status.HTTP_200_OK, summary="Retrain Models on New Baseline Data")
def retrain_anomaly_models():
    return engine.train_models([])


@router.get("/models", status_code=status.HTTP_200_OK, summary="List Active Anomaly Models & Versions")
def get_anomaly_models():
    return {
        "models": [
            {"model_id": "MOD-STAT-01", "name": "StatisticalDetector", "version": "v1.0.0", "status": "active"},
            {"model_id": "MOD-IF-02", "name": "IsolationForestDetector", "version": "v1.0.0", "status": "active"},
            {"model_id": "MOD-PEER-03", "name": "PeerGroupDetector", "version": "v1.0.0", "status": "active"},
            {"model_id": "MOD-DRIFT-04", "name": "BehaviourDriftDetector", "version": "v1.0.0", "status": "active"},
            {"model_id": "MOD-SEQ-05", "name": "SequenceBehaviourDetector", "version": "v1.0.0", "status": "active"}
        ]
    }


@router.get("/history", status_code=status.HTTP_200_OK, summary="Get Historical Anomaly Inference Logs")
def get_anomaly_history():
    return {"history": AnomalyRepository.get_inference_history()}


@router.get("/detectors", status_code=status.HTTP_200_OK, summary="Get Registered Anomaly Detectors & Default Weights")
def get_detectors():
    detectors_meta = [d.metadata() for d in engine.registry.get_all_detectors().values()]
    return {
        "detectors": detectors_meta,
        "default_weights": {
            "StatisticalDetector": 0.25,
            "IsolationForestDetector": 0.25,
            "PeerGroupDetector": 0.20,
            "BehaviourDriftDetector": 0.15,
            "SequenceBehaviourDetector": 0.15
        }
    }
