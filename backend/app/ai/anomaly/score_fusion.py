from typing import Dict, Any


class ScoreFusionEngine:
    """Combines individual detector scores into a normalized Hybrid Anomaly Score [0.0, 1.0]."""

    DEFAULT_WEIGHTS = {
        "StatisticalDetector": 0.25,
        "IsolationForestDetector": 0.25,
        "PeerGroupDetector": 0.20,
        "BehaviourDriftDetector": 0.15,
        "SequenceBehaviourDetector": 0.15
    }

    @staticmethod
    def fuse_scores(detector_scores: Dict[str, float], custom_weights: Dict[str, float] = None) -> Dict[str, Any]:
        weights = custom_weights or ScoreFusionEngine.DEFAULT_WEIGHTS
        total_weight = sum(weights.get(name, 0.2) for name in detector_scores.keys())

        if total_weight <= 0:
            total_weight = 1.0

        hybrid_score = 0.0
        contributions: Dict[str, float] = {}

        for name, score in detector_scores.items():
            w = weights.get(name, 0.2)
            weighted_contrib = (score * w) / total_weight
            hybrid_score += weighted_contrib
            contributions[name] = round(weighted_contrib, 4)

        final_hybrid_score = round(min(1.0, max(0.0, hybrid_score)), 4)

        return {
            "hybrid_anomaly_score": final_hybrid_score,
            "detector_scores": {k: round(v, 4) for k, v in detector_scores.items()},
            "detector_contributions": contributions,
            "weights_used": weights
        }
