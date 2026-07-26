from abc import ABC, abstractmethod
from typing import Dict, Any, List


class BaseDetector(ABC):
    """Abstract Base Class interface for pluggable anomaly detectors."""

    @abstractmethod
    def fit(self, training_data: List[Dict[str, Any]]) -> None:
        """Fit or train model parameters."""
        pass

    @abstractmethod
    def score(self, event: Dict[str, Any], profile: Dict[str, Any]) -> float:
        """Score event anomaly in range [0.0, 1.0]."""
        pass

    @abstractmethod
    def validate(self, test_data: List[Dict[str, Any]]) -> Dict[str, float]:
        """Validate detector performance metrics."""
        pass

    @abstractmethod
    def metadata(self) -> Dict[str, Any]:
        """Return detector metadata and configuration."""
        pass
