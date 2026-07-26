from typing import Dict, Any
from fastapi import APIRouter, Depends, status, Body
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.ai.context.context_engine import ContextEngine
from app.ai.context.context_repository import ContextRepository
from app.ai.context.trust_reasoning import TrustReasoningEngine
from app.ai.context.policy_reasoning import PolicyReasoningEngine
from app.ai.context.calendar_reasoning import CalendarReasoningEngine
from app.ai.context.relationship_reasoning import RelationshipReasoningEngine
from app.ai.profiling.profile_manager import ProfileManager

router = APIRouter()


@router.post("/evaluate", status_code=status.HTTP_200_OK, summary="Evaluate Event Context & Hybrid Anomaly Score")
def evaluate_context(
    payload: Dict[str, Any] = Body(
        default={
            "event": {
                "event_id": "evt_sim_99182",
                "entity_id": "alex.smith1@bip.com",
                "login_hour": 3,
                "session_duration_minutes": 15,
                "resource_accessed": "AWS Production Console",
                "vpn_used": False,
                "mfa_verified": False,
                "threat_label": "Credential Stuffing"
            },
            "hybrid_anomaly_score": 0.825
        }
    ),
    db: Session = Depends(get_db)
):
    event = payload.get("event", payload)
    hybrid_score = payload.get("hybrid_anomaly_score")
    engine = ContextEngine(db)
    return engine.evaluate_event_context(event, hybrid_score)


@router.get("/history", status_code=status.HTTP_200_OK, summary="Get Historical Context Assessment Logs")
def get_context_history():
    return {
        "history": ContextRepository.get_history(),
        "metrics": ContextRepository.get_evaluation_metrics()
    }


@router.get("/reasoning/{id}", status_code=status.HTTP_200_OK, summary="Get Structured Reasoning Trace")
def get_reasoning_trace(id: str, db: Session = Depends(get_db)):
    mock_event = {"entity_id": id, "login_hour": 9, "resource_accessed": "Azure Active Directory"}
    engine = ContextEngine(db)
    res = engine.evaluate_event_context(mock_event, 0.10)
    return {
        "assessment_id": f"ctx_eval_{id}",
        "reasoning_trace": res["reasoning_trace"],
        "supporting_evidence": res["supporting_evidence"],
        "contradicting_evidence": res["contradicting_evidence"]
    }


@router.get("/trust/{id}", status_code=status.HTTP_200_OK, summary="Get Entity Trust Reasoning Breakdown")
def get_trust_breakdown(id: str, db: Session = Depends(get_db)):
    profile = ProfileManager(db).get_or_create_profile(id, "user")
    mock_event = {"entity_id": id, "device_id": f"dev_{id}", "mfa_verified": True, "vpn_used": True}
    return TrustReasoningEngine.evaluate_trust(mock_event, profile)


@router.get("/policies/{id}", status_code=status.HTTP_200_OK, summary="Get Entity Policy Reasoning Breakdown")
def get_policy_breakdown(id: str, db: Session = Depends(get_db)):
    profile = ProfileManager(db).get_or_create_profile(id, "user")
    mock_event = {"entity_id": id, "resource_accessed": "AWS Production Console"}
    return PolicyReasoningEngine.evaluate_policy(mock_event, profile)


@router.get("/calendar/{id}", status_code=status.HTTP_200_OK, summary="Get Entity Calendar Reasoning Breakdown")
def get_calendar_breakdown(id: str, db: Session = Depends(get_db)):
    profile = ProfileManager(db).get_or_create_profile(id, "user")
    mock_event = {"entity_id": id, "login_hour": 3}
    return CalendarReasoningEngine.evaluate_calendar(mock_event, profile)


@router.get("/relationships/{id}", status_code=status.HTTP_200_OK, summary="Get Entity Relationship Graph Reasoning")
def get_relationship_breakdown(id: str, db: Session = Depends(get_db)):
    profile = ProfileManager(db).get_or_create_profile(id, "user")
    mock_event = {"entity_id": id, "resource_accessed": "GitHub Enterprise"}
    return RelationshipReasoningEngine.evaluate_relationships(mock_event, profile)
