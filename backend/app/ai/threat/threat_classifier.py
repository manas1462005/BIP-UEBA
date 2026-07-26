from typing import Dict, Any, List

TAXONOMY_CATEGORIES = [
    "Normal Baseline",
    "Brute Force",
    "Impossible Travel",
    "Credential Stuffing",
    "Lateral Movement",
    "Device Spoofing",
    "Low-and-Slow Exfiltration",
    "Insider Drift"
]


class ThreatClassifier:
    """Classifies primary threat category using deterministic evidence & hypothesis weighting."""

    @staticmethod
    def classify_threat(evidence: Dict[str, Any], hypotheses: List[Dict[str, Any]]) -> Dict[str, Any]:
        primary_hypothesis = hypotheses[0] if hypotheses else {
            "hypothesis_name": "Normal Baseline Workday Activity",
            "probability": 0.95,
            "confidence": 0.95
        }

        prob = primary_hypothesis.get("probability", 0.95)
        name = primary_hypothesis.get("hypothesis_name", "Normal Baseline")

        if "Brute Force" in name:
            category = "Brute Force"
            tactic_code = "TA0006"
        elif "Impossible Travel" in name:
            category = "Impossible Travel"
            tactic_code = "TA0001"
        elif "Credential Theft" in name or "Credential Spray" in name or "Credential Compromise" in name or "Credential Stuffing" in name:
            category = "Credential Stuffing"
            tactic_code = "TA0006"
        elif "Lateral Movement" in name:
            category = "Lateral Movement"
            tactic_code = "TA0008"
        elif "Device Spoofing" in name:
            category = "Device Spoofing"
            tactic_code = "TA0005"
        elif "Low-and-Slow" in name or "Exfiltration" in name:
            category = "Low-and-Slow Exfiltration"
            tactic_code = "TA0010"
        elif "Insider" in name or "Drift" in name:
            category = "Insider Drift"
            tactic_code = "TA0009"
        else:
            category = "Normal Baseline"
            tactic_code = "BENIGN-NORM"

        return {
            "primary_threat_category": category,
            "primary_hypothesis_name": name,
            "classification_confidence": primary_hypothesis.get("confidence", 0.90),
            "primary_tactic_code": tactic_code,
            "probability_top1": prob
        }
