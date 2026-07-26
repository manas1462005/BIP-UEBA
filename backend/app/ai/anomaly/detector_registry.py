from typing import Dict, List
from app.ai.anomaly.base_detector import BaseDetector
from app.ai.anomaly.statistical_detector import StatisticalDetector
from app.ai.anomaly.isolation_forest_detector import IsolationForestDetector
from app.ai.anomaly.peer_group_detector import PeerGroupDetector
from app.ai.anomaly.drift_detector import BehaviourDriftDetector
from app.ai.anomaly.sequence_detector import SequenceBehaviourDetector


class DetectorRegistry:
    """Registry managing pluggable anomaly detectors."""

    def __init__(self):
        self._detectors: Dict[str, BaseDetector] = {}
        self.register_default_detectors()

    def register(self, detector: BaseDetector) -> None:
        name = detector.metadata()["name"]
        self._detectors[name] = detector

    def get_all_detectors(self) -> Dict[str, BaseDetector]:
        return self._detectors

    def register_default_detectors(self) -> None:
        self.register(StatisticalDetector())
        self.register(IsolationForestDetector())
        self.register(PeerGroupDetector())
        self.register(BehaviourDriftDetector())
        self.register(SequenceBehaviourDetector())
