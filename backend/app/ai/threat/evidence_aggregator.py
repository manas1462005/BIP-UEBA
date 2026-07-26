from typing import Dict, Any, List


class EvidenceAggregator:
    """Aggregates multi-phase evidence into a structured evidence graph."""

    @staticmethod
    def aggregate_evidence(
        event: Dict[str, Any],
        profile: Dict[str, Any],
        anomaly_result: Dict[str, Any],
        context_result: Dict[str, Any]
    ) -> Dict[str, Any]:
        
        hybrid_score = anomaly_result.get("hybrid_anomaly_score", 0.05)
        context_assessment = context_result.get("context_assessment", "Verified Normal Activity Baseline")
        trust_summary = context_result.get("trust_summary", "High Trust")
        calendar_summary = context_result.get("calendar_summary", "Standard Weekday Work Schedule")
        threat_label = event.get("threat_label", "Benign")

        evidence_signals: List[Dict[str, Any]] = [
            {"source": "Hybrid Anomaly Ensemble", "type": "Anomaly Metric", "value": f"Score {hybrid_score:.3f}"},
            {"source": "Context Reasoning Engine", "type": "Context Verdict", "value": context_assessment},
            {"source": "Trust Reasoning Engine", "type": "Hardware/Auth Trust", "value": trust_summary},
            {"source": "Calendar Reasoning Engine", "type": "Schedule Driver", "value": calendar_summary},
            {"source": "Telemetry Ingestion", "type": "Ground Truth Label", "value": threat_label}
        ]

        return {
            "entity_id": event.get("entity_id", "alex.smith1@bip.com"),
            "event_id": event.get("event_id", "evt_sim_99182"),
            "hybrid_score": hybrid_score,
            "context_assessment": context_assessment,
            "trust_summary": trust_summary,
            "calendar_summary": calendar_summary,
            "threat_label": threat_label,
            "evidence_signals": evidence_signals,
            "detector_scores": anomaly_result.get("detector_scores", {}),
            "reasoning_trace": context_result.get("reasoning_trace", [])
        }
