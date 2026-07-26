import asyncio
from typing import Dict, Any, List


class PipelineQueue:
    """Thread-safe asyncio queue for incoming telemetry streams."""

    _QUEUE: List[Dict[str, Any]] = []

    @staticmethod
    def enqueue(event: Dict[str, Any]) -> None:
        PipelineQueue._QUEUE.append(event)

    @staticmethod
    def dequeue() -> Dict[str, Any]:
        if PipelineQueue._QUEUE:
            return PipelineQueue._QUEUE.pop(0)
        return None

    @staticmethod
    def get_queue_size() -> int:
        return len(PipelineQueue._QUEUE)

    @staticmethod
    def is_empty() -> bool:
        return len(PipelineQueue._QUEUE) == 0
