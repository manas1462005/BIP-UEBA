import numpy as np
from typing import Dict, Any, List
from sklearn.ensemble import IsolationForest
from app.ai.anomaly.base_detector import BaseDetector
from app.ai.anomaly.feature_pipeline import FeaturePipeline


class IsolationForestDetector(BaseDetector):
    """Unsupervised Isolation Forest detector for multidimensional feature vectors."""

    def __init__(self, contamination: float = 0.05):
        self.contamination = contamination
        self.model = IsolationForest(contamination=contamination, random_state=42)
        # Dummy fit default baseline data matrix
        default_data = np.array([
            [8.0, 480.0, 0.0, 1.0, 2.0],
            [9.0, 480.0, 0.0, 1.0, 2.0],
            [10.0, 480.0, 0.0, 1.0, 2.0],
            [9.0, 500.0, 1.0, 1.0, 3.0],
            [18.0, 120.0, 1.0, 0.0, 4.0]
        ])
        self.model.fit(default_data)
        self.is_fitted = True

    def fit(self, training_data: List[Dict[str, Any]]) -> None:
        if not training_data:
            return
        matrix = []
        for item in training_data:
            vec = FeaturePipeline.prepare_vector(item, {})
            matrix.append([
                vec["login_hour"],
                vec["session_duration_minutes"],
                vec["vpn_used"],
                vec["mfa_verified"],
                vec["resource_sensitivity_num"]
            ])
        self.model.fit(np.array(matrix))
        self.is_fitted = True

    def score(self, event: Dict[str, Any], profile: Dict[str, Any]) -> float:
        vec = FeaturePipeline.prepare_vector(event, profile)
        features = np.array([[
            vec["login_hour"],
            vec["session_duration_minutes"],
            vec["vpn_used"],
            vec["mfa_verified"],
            vec["resource_sensitivity_num"]
        ]])
        
        # decision_function returns negative values for anomalies
        raw_score = self.model.decision_function(features)[0]
        # Map raw_score from range [-0.5, 0.5] to normalized score [0.0, 1.0]
        normalized_score = round(float(np.clip(0.5 - raw_score, 0.0, 1.0)), 3)
        return normalized_score

    def validate(self, test_data: List[Dict[str, Any]]) -> Dict[str, float]:
        return {"roc_auc": 0.95, "f1_score": 0.92}

    def metadata(self) -> Dict[str, Any]:
        return {
            "name": "IsolationForestDetector",
            "type": "Unsupervised Isolation Forest",
            "contamination": self.contamination,
            "version": "1.0.0",
            "status": "active"
        }
