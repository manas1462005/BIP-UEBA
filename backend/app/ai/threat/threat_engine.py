import time
from typing import Dict, Any, List
from sqlalchemy.orm import Session
from app.ai.threat.evidence_aggregator import EvidenceAggregator
from app.ai.threat.hypothesis_engine import ThreatHypothesisEngine
from app.ai.threat.threat_classifier import ThreatClassifier
from app.ai.threat.mitre_mapper import MITREMapper
from app.ai.threat.attack_chain_builder import AttackChainBuilder
from app.ai.threat.threat_repository import ThreatRepository
from app.ai.context.context_engine import ContextEngine
from app.ai.anomaly.hybrid_engine import HybridEngine
from app.ai.profiling.profile_manager import ProfileManager


class ThreatEngine:
    """Orchestrates evidence aggregation, hypothesis generation, classification, & MITRE mapping."""

    def __init__(self, db: Session):
        self.db = db
        self.context_engine = ContextEngine(db)
        self.hybrid_engine = HybridEngine()

    def evaluate_threat(self, event: Dict[str, Any], anomaly_result: Dict[str, Any] = None, context_result: Dict[str, Any] = None) -> Dict[str, Any]:
        start_time = time.time()
        entity_id = event.get("entity_id", "alex.smith1@bip.com")
        profile = ProfileManager(self.db).get_or_create_profile(entity_id, "user")

        if anomaly_result is None:
            anomaly_result = self.hybrid_engine.evaluate_event(event, profile)

        if context_result is None:
            context_result = self.context_engine.evaluate_event_context(event, anomaly_result["hybrid_anomaly_score"])

        # Step 1: Evidence Aggregation
        evidence = EvidenceAggregator.aggregate_evidence(event, profile, anomaly_result, context_result)

        # Step 2: Hypothesis Generation & Ranking
        hypotheses = ThreatHypothesisEngine.generate_hypotheses(evidence)

        # Step 3: Threat Classification
        classification = ThreatClassifier.classify_threat(evidence, hypotheses)

        # Step 4: MITRE ATT&CK Mapping
        mitre_mappings = MITREMapper.map_mitre_attack(classification["primary_threat_category"])

        # Step 5: Attack Chain Construction
        attack_chain = AttackChainBuilder.build_attack_chain(classification["primary_threat_category"], evidence)

        elapsed_ms = round((time.time() - start_time) * 1000, 2)

        assessment = {
            "threat_id": f"tht_eval_{event.get('event_id', 'sim_001')}",
            "event_id": event.get("event_id", "evt_sim_99182"),
            "entity_id": entity_id,
            "primary_classification": classification,
            "ranked_hypotheses": hypotheses,
            "mitre_mappings": mitre_mappings,
            "attack_chain": attack_chain,
            "evidence_summary": evidence,
            "classification_time_ms": elapsed_ms
        }

        ThreatRepository.save_threat_assessment(assessment)
        return assessment
