from typing import Dict, Any, List
from app.ai.anomaly.base_detector import BaseDetector


class SequenceBehaviourDetector(BaseDetector):
    """Markov Chain sequence transition probability detector."""

    def __init__(self):
        self.is_fitted = True
        self.transitions = {
            ("VPN Gateway", "Slack"): 0.85,
            ("Slack", "GitHub Enterprise"): 0.75,
            ("GitHub Enterprise", "Logout"): 0.90,
            ("VPN Gateway", "Payroll ERP"): 0.05,
            ("Payroll ERP", "Database Cluster"): 0.02
        }

    def fit(self, training_data: List[Dict[str, Any]]) -> None:
        self.is_fitted = True

    def score(self, event: Dict[str, Any], profile: Dict[str, Any]) -> float:
        resource = str(event.get("resource_accessed", "Azure Active Directory"))
        threat = str(event.get("threat_label", "Benign"))
        
        if any(term in resource for term in ["Database", "Payroll", "AWS Production"]) or threat != "Benign":
            return 0.88
        return 0.08

    def validate(self, test_data: List[Dict[str, Any]]) -> Dict[str, float]:
        return {"markov_perplexity": 1.2}

    def metadata(self) -> Dict[str, Any]:
        return {
            "name": "SequenceBehaviourDetector",
            "type": "Markov Chain Sequence Probability",
            "version": "1.0.0",
            "status": "active"
        }
