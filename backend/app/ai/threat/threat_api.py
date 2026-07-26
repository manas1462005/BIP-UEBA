from typing import Dict, Any
from fastapi import APIRouter, Depends, status, Body
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.ai.threat.threat_engine import ThreatEngine
from app.ai.threat.threat_repository import ThreatRepository

router = APIRouter()


@router.post("/classify", status_code=status.HTTP_200_OK, summary="Classify Threat & Rank Hypotheses")
def classify_threat_event(
    event: Dict[str, Any] = Body(
        default={
            "event_id": "evt_sim_99182",
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
    engine = ThreatEngine(db)
    return engine.evaluate_threat(event)


@router.get("/history", status_code=status.HTTP_200_OK, summary="Get Threat Assessment Logs & Evaluation Metrics")
def get_threat_history():
    return {
        "history": ThreatRepository.get_history(),
        "evaluation_metrics": ThreatRepository.get_evaluation_metrics()
    }


@router.get("/hypotheses/{id}", status_code=status.HTTP_200_OK, summary="Get Ranked Threat Hypotheses")
def get_hypotheses_breakdown(id: str, db: Session = Depends(get_db)):
    engine = ThreatEngine(db)
    res = engine.evaluate_threat({"entity_id": id, "event_id": f"evt_{id}"})
    return {
        "threat_id": res["threat_id"],
        "ranked_hypotheses": res["ranked_hypotheses"]
    }


@router.get("/mitre/{id}", status_code=status.HTTP_200_OK, summary="Get MITRE ATT&CK Mapping")
def get_mitre_mapping(id: str, db: Session = Depends(get_db)):
    engine = ThreatEngine(db)
    res = engine.evaluate_threat({"entity_id": id, "event_id": f"evt_{id}"})
    return {
        "threat_id": res["threat_id"],
        "mitre_mappings": res["mitre_mappings"]
    }


@router.get("/attack-chain/{id}", status_code=status.HTTP_200_OK, summary="Get Multi-Stage Attack Progression Graph")
def get_attack_chain(id: str, db: Session = Depends(get_db)):
    engine = ThreatEngine(db)
    res = engine.evaluate_threat({"entity_id": id, "event_id": f"evt_{id}"})
    return {
        "threat_id": res["threat_id"],
        "attack_chain": res["attack_chain"]
    }


@router.get("/{id}", status_code=status.HTTP_200_OK, summary="Get Threat Assessment Details by ID")
def get_threat_assessment(id: str, db: Session = Depends(get_db)):
    engine = ThreatEngine(db)
    return engine.evaluate_threat({"entity_id": id, "event_id": f"evt_{id}"})
