import time
from typing import Dict, Any
from sqlalchemy.orm import Session
from app.ai.profiling.profile_manager import ProfileManager
from app.ai.anomaly.hybrid_engine import HybridEngine
from app.ai.context.context_engine import ContextEngine
from app.ai.threat.threat_engine import ThreatEngine
from app.ai.explainability.explanation_engine import ExplanationEngine
from app.pipeline.pipeline_repository import PipelineRepository


class EventPipeline:
    """Orchestrates single event execution through all 5 AI phases in sequence."""

    def __init__(self, db: Session):
        self.db = db
        self.profile_manager = ProfileManager(db)
        self.hybrid_engine = HybridEngine()
        self.context_engine = ContextEngine(db)
        self.threat_engine = ThreatEngine(db)
        self.explanation_engine = ExplanationEngine(db)

    def process_event(self, event: Dict[str, Any]) -> Dict[str, Any]:
        start_pipeline = time.time()
        entity_id = event.get("entity_id", "alex.smith1@bip.com")
        event_id = event.get("event_id", f"evt_sim_{int(time.time()*1000)}")

        # Stage 1: Feature Extraction & Profile Update
        t0 = time.time()
        profile = self.profile_manager.get_or_create_profile(entity_id, "user")
        t_profiling = round((time.time() - t0) * 1000, 2)
        PipelineRepository.record_stage_timing("behaviour_profiling", t_profiling)

        # Stage 2: Hybrid Anomaly Detection
        t0 = time.time()
        anomaly_res = self.hybrid_engine.evaluate_event(event, profile)
        t_anomaly = round((time.time() - t0) * 1000, 2)
        PipelineRepository.record_stage_timing("anomaly_detection", t_anomaly)

        # Stage 3: Context Reasoning
        t0 = time.time()
        context_res = self.context_engine.evaluate_event_context(event, anomaly_res["hybrid_anomaly_score"])
        t_context = round((time.time() - t0) * 1000, 2)
        PipelineRepository.record_stage_timing("context_reasoning", t_context)

        # Stage 4: Threat Classification
        t0 = time.time()
        threat_res = self.threat_engine.evaluate_threat(event, anomaly_res, context_res)
        t_threat = round((time.time() - t0) * 1000, 2)
        PipelineRepository.record_stage_timing("threat_classification", t_threat)

        # Stage 5: Explainability Report Generation
        t0 = time.time()
        explanation_res = self.explanation_engine.generate_full_explanation(event, threat_res)
        t_explain = round((time.time() - t0) * 1000, 2)
        PipelineRepository.record_stage_timing("explainability_generation", t_explain)

        total_latency = round((time.time() - start_pipeline) * 1000, 2)

        pipeline_result = {
            "event_id": event_id,
            "entity_id": entity_id,
            "hybrid_anomaly_score": anomaly_res["hybrid_anomaly_score"],
            "context_assessment": context_res["context_assessment"],
            "primary_threat_category": threat_res["primary_classification"]["primary_threat_category"],
            "total_latency_ms": total_latency,
            "stage_latencies": {
                "profiling_ms": t_profiling,
                "anomaly_ms": t_anomaly,
                "context_ms": t_context,
                "threat_ms": t_threat,
                "explainability_ms": t_explain
            },
            "explanation_report": explanation_res
        }

        PipelineRepository.record_event_processed({
            "timestamp": time.strftime("%H:%M:%S UTC"),
            "event_id": event_id,
            "entity_id": entity_id,
            "hybrid_score": anomaly_res["hybrid_anomaly_score"],
            "category": threat_res["primary_classification"]["primary_threat_category"],
            "total_latency_ms": total_latency
        })

        return pipeline_result
