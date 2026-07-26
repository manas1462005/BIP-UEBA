from typing import Dict, Any
from fastapi import APIRouter, Depends, status, Body
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.ai.explainability.explanation_engine import ExplanationEngine
from app.ai.explainability.report_generator import ReportGenerator

router = APIRouter()


@router.post("/generate", status_code=status.HTTP_200_OK, summary="Generate Full Evidence-Grounded Explanation Report")
def generate_explanation(
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
            }
        }
    ),
    db: Session = Depends(get_db)
):
    event = payload.get("event", payload)
    engine = ExplanationEngine(db)
    return engine.generate_full_explanation(event)


@router.get("/report/full", status_code=status.HTTP_200_OK, summary="Generate Complete 6-Section Investigation Report")
def generate_full_report(
    entity_id: str = "alex.smith1@bip.com",
    event_id: str = "evt_sim_99182",
    db: Session = Depends(get_db)
):
    generator = ReportGenerator(db)
    return generator.generate_full_investigation_report({
        "entity_id": entity_id,
        "event_id": event_id,
        "login_hour": 3,
        "resource_accessed": "AWS Production Console",
        "threat_label": "Credential Stuffing"
    })


@router.post("/copilot", status_code=status.HTTP_200_OK, summary="Ask Analyst Copilot Grounded Q&A Assistant")
def ask_copilot_assistant(
    payload: Dict[str, Any] = Body(
        default={
            "event": {
                "event_id": "evt_sim_99182",
                "entity_id": "alex.smith1@bip.com",
                "login_hour": 3,
                "resource_accessed": "AWS Production Console"
            },
            "query": "Why was this event classified as Credential Stuffing?"
        }
    ),
    db: Session = Depends(get_db)
):
    event = payload.get("event", {})
    query = payload.get("query", "Why was this classified?")
    engine = ExplanationEngine(db)
    return engine.ask_copilot(event, query)


@router.get("/timeline/{id}", status_code=status.HTTP_200_OK, summary="Get Chronological Investigation Timeline")
def get_timeline(id: str, db: Session = Depends(get_db)):
    engine = ExplanationEngine(db)
    report = engine.generate_full_explanation({"entity_id": id, "event_id": f"evt_{id}"})
    return {
        "explanation_id": report["explanation_id"],
        "timeline": report["timeline"]
    }


@router.get("/evidence/{id}", status_code=status.HTTP_200_OK, summary="Get Queryable Evidence Graph Metadata")
def get_evidence_graph(id: str, db: Session = Depends(get_db)):
    engine = ExplanationEngine(db)
    report = engine.generate_full_explanation({"entity_id": id, "event_id": f"evt_{id}"})
    return {
        "explanation_id": report["explanation_id"],
        "evidence_package": report["evidence_package"]
    }


@router.get("/recommendations/{id}", status_code=status.HTTP_200_OK, summary="Get SOC Analyst Action Checklist")
def get_recommendations(id: str, db: Session = Depends(get_db)):
    engine = ExplanationEngine(db)
    report = engine.generate_full_explanation({"entity_id": id, "event_id": f"evt_{id}"})
    return {
        "explanation_id": report["explanation_id"],
        "recommendations": report["recommendations"]
    }


@router.get("/{id}", status_code=status.HTTP_200_OK, summary="Get Cached Explanation Report by ID")
def get_explanation_report(id: str, db: Session = Depends(get_db)):
    engine = ExplanationEngine(db)
    return engine.generate_full_explanation({"entity_id": id, "event_id": f"evt_{id}"})
