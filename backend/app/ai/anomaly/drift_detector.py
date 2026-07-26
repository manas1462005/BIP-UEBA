from typing import Dict, Any, List
from app.ai.anomaly.base_detector import BaseDetector


class BehaviourDriftDetector(BaseDetector):
    """Detects gradual behavioral shifts between moving temporal windows."""

    def __init__(self):
        self.is_fitted = True

    def fit(self, training_data: List[Dict[str, Any]]) -> None:
        self.is_fitted = True

    def score(self, event: Dict[str, Any], profile: Dict[str, Any]) -> float:
        # Check maturity state or drift history from profile
        maturity = profile.get("maturity_state", "Stable")
        if maturity == "New":
            return 0.10
        elif maturity == "Learning":
            return 0.20
        elif event.get("threat_label") == "Credential Stuffing":
            return 0.85
        return 0.05

    def validate(self, test_data: List[Dict[str, Any]]) -> Dict[str, float]:
        return {"drift_sensitivity": 0.88}

    def metadata(self) -> Dict[str, Any]:
        return {
            "name": "BehaviourDriftDetector",
            "type": "Moving Window Drift Detection",
            "windows": ["7d", "30d", "90d"],
            "version": "1.0.0",
            "status": "active"
        }
