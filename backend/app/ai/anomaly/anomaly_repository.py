from typing import Dict, Any, List


class AnomalyRepository:
    """In-memory & PostgreSQL repository for anomaly model metadata & inference history."""

    _INFERENCE_LOGS: List[Dict[str, Any]] = []

    @staticmethod
    def log_inference(result: Dict[str, Any]) -> None:
        AnomalyRepository._INFERENCE_LOGS.append(result)
        if len(AnomalyRepository._INFERENCE_LOGS) > 500:
            AnomalyRepository._INFERENCE_LOGS.pop(0)

    @staticmethod
    def get_inference_history() -> List[Dict[str, Any]]:
        return AnomalyRepository._INFERENCE_LOGS
