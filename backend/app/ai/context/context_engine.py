import time
from typing import Dict, Any
from sqlalchemy.orm import Session
from app.ai.context.reasoning_pipeline import ReasoningPipeline
from app.ai.context.context_repository import ContextRepository
from app.ai.profiling.profile_manager import ProfileManager
from app.ai.anomaly.hybrid_engine import HybridEngine


class ContextEngine:
    """High-level orchestrator for Context Intelligence & Reasoning."""

    def __init__(self, db: Session):
        self.db = db
        self.hybrid_engine = HybridEngine()

    def evaluate_event_context(self, event: Dict[str, Any], hybrid_score: float = None) -> Dict[str, Any]:
        start_time = time.time()
        entity_id = event.get("entity_id", "alex.smith1@bip.com")
        profile = ProfileManager(self.db).get_or_create_profile(entity_id, "user")

        if hybrid_score is None:
            anomaly_res = self.hybrid_engine.evaluate_event(event, profile)
            hybrid_score = anomaly_res["hybrid_anomaly_score"]

        assessment = ReasoningPipeline.execute(event, profile, hybrid_score)
        eval_time = round((time.time() - start_time) * 1000, 2)
        assessment["evaluation_time_ms"] = eval_time

        ContextRepository.save_assessment(assessment)
        return assessment
