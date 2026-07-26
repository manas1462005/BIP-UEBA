import time
from typing import Dict, Any
from sqlalchemy.orm import Session
from app.ai.explainability.grounding_engine import GroundingEngine
from app.ai.explainability.timeline_builder import TimelineBuilder
from app.ai.explainability.executive_summary import ExecutiveSummaryEngine
from app.ai.explainability.technical_summary import TechnicalSummaryEngine
from app.ai.explainability.recommendation_engine import RecommendationEngine
from app.ai.explainability.citation_engine import CitationEngine
from app.ai.explainability.copilot_engine import AnalystCopilotEngine
from app.ai.explainability.explainability_repository import ExplainabilityRepository
from app.ai.threat.threat_engine import ThreatEngine


class ExplanationEngine:
    """Orchestrates evidence package sealing, timelines, summaries, & copilot Q&A."""

    def __init__(self, db: Session):
        self.db = db
        self.threat_engine = ThreatEngine(db)

    def generate_full_explanation(self, event: Dict[str, Any], threat_assessment: Dict[str, Any] = None) -> Dict[str, Any]:
        start_time = time.time()

        if threat_assessment is None:
            threat_assessment = self.threat_engine.evaluate_threat(event)

        # Step 1: Seal Evidence Package & Build Graph
        evidence_package = GroundingEngine.build_evidence_package(event, threat_assessment)

        # Step 2: Build Investigation Timeline
        timeline = TimelineBuilder.build_timeline(evidence_package)

        # Step 3: Executive Summary
        exec_summary = ExecutiveSummaryEngine.generate_summary(evidence_package)

        # Step 4: Technical Analyst Narrative + Citations
        tech_narrative = TechnicalSummaryEngine.generate_narrative(evidence_package)
        cited_narrative = CitationEngine.attach_citations(tech_narrative["technical_narrative"], evidence_package)
        tech_narrative["technical_narrative_cited"] = cited_narrative

        # Step 5: Recommendations
        recommendations = RecommendationEngine.generate_recommendations(evidence_package)

        elapsed_ms = round((time.time() - start_time) * 1000, 2)

        report = {
            "explanation_id": f"exp_report_{event.get('event_id', 'sim_001')}",
            "event_id": event.get("event_id", "evt_sim_99182"),
            "entity_id": event.get("entity_id", "alex.smith1@bip.com"),
            "executive_summary": exec_summary,
            "technical_summary": tech_narrative,
            "timeline": timeline,
            "recommendations": recommendations,
            "evidence_package": evidence_package,
            "generation_time_ms": elapsed_ms
        }

        ExplainabilityRepository.save_explanation(report)
        return report

    def ask_copilot(self, event: Dict[str, Any], query: str) -> Dict[str, Any]:
        threat_assessment = self.threat_engine.evaluate_threat(event)
        evidence_package = GroundingEngine.build_evidence_package(event, threat_assessment)
        return AnalystCopilotEngine.answer_query(query, evidence_package)
