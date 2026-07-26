from typing import Dict, Any, List


class ThreatHypothesisEngine:
    """Generates and ranks multiple probabilistic threat hypotheses P(H_i | E)."""

    @staticmethod
    def generate_hypotheses(evidence: Dict[str, Any]) -> List[Dict[str, Any]]:
        hybrid_score = evidence.get("hybrid_score", 0.05)
        assessment = evidence.get("context_assessment", "")
        threat_label = evidence.get("threat_label", "Benign")

        hypotheses: List[Dict[str, Any]] = []

        if threat_label == "Brute Force" or "Brute Force" in threat_label:
            hypotheses.append({
                "hypothesis_name": "Brute Force Password Spray Attack",
                "category": "Brute Force",
                "probability": 0.85,
                "confidence": 0.92,
                "supporting_evidence": ["Multiple failed auth attempts", "Unverified MFA"],
                "contradicting_evidence": []
            })
        elif threat_label in ["Credential Stuffing", "Credential Theft"] or (hybrid_score > 0.70 and "Unjustified" in assessment):
            hypotheses.append({
                "hypothesis_name": "Credential Theft & Password Spray Attack",
                "category": "Credential Compromise",
                "probability": 0.80,
                "confidence": 0.90,
                "supporting_evidence": ["High statistical Z-score deviation", "Unmanaged endpoint", "Unverified MFA authentication attempt"],
                "contradicting_evidence": []
            })
            hypotheses.append({
                "hypothesis_name": "Lateral Movement via STS AssumeRole",
                "category": "Lateral Movement",
                "probability": 0.15,
                "confidence": 0.80,
                "supporting_evidence": ["Targeted AWS Production Console access"],
                "contradicting_evidence": []
            })
        elif threat_label == "Impossible Travel":
            hypotheses.append({
                "hypothesis_name": "Impossible Travel Anomaly",
                "category": "Impossible Travel",
                "probability": 0.88,
                "confidence": 0.94,
                "supporting_evidence": ["Geographic distance / time window contradiction"],
                "contradicting_evidence": []
            })
        else:
            hypotheses.append({
                "hypothesis_name": "Normal Baseline Enterprise Activity",
                "category": "Normal Baseline",
                "probability": 0.95,
                "confidence": 0.98,
                "supporting_evidence": ["Baseline hours match typical window", "Known corporate IP & managed hardware"],
                "contradicting_evidence": []
            })

        hypotheses.sort(key=lambda x: x["probability"], reverse=True)
        return hypotheses
