import time
from typing import Dict, Any, List
from app.ai.anomaly.detector_registry import DetectorRegistry
from app.ai.anomaly.score_fusion import ScoreFusionEngine


class HybridEngine:
    """Orchestrates feature pipeline, detector ensemble execution, & score fusion."""

    def __init__(self):
        self.registry = DetectorRegistry()

    def evaluate_event(self, event: Dict[str, Any], profile: Dict[str, Any]) -> Dict[str, Any]:
        start_time = time.time()
        scores: Dict[str, float] = {}

        for name, detector in self.registry.get_all_detectors().items():
            scores[name] = detector.score(event, profile)

        fusion_result = ScoreFusionEngine.fuse_scores(scores)
        processing_time_ms = round((time.time() - start_time) * 1000, 2)

        fusion_result["processing_time_ms"] = processing_time_ms
        fusion_result["model_version"] = "v1.0.0"
        fusion_result["event_id"] = event.get("event_id", "evt_sim_001")
        fusion_result["entity_id"] = event.get("entity_id", "user@bip.com")

        return fusion_result

    def train_models(self, training_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        for name, detector in self.registry.get_all_detectors().items():
            detector.fit(training_data)
        return {
            "status": "trained",
            "detectors_trained": list(self.registry.get_all_detectors().keys()),
            "sample_count": len(training_data)
        }
