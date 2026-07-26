from typing import Dict, Any, List
from sqlalchemy.orm import Session
from app.pipeline.pipeline_queue import PipelineQueue
from app.pipeline.event_pipeline import EventPipeline


class PipelineManager:
    """Manages event queueing and batch processing through EventPipeline."""

    @staticmethod
    def enqueue_event(event: Dict[str, Any]) -> None:
        PipelineQueue.enqueue(event)

    @staticmethod
    def process_next_event(db: Session) -> Dict[str, Any]:
        event = PipelineQueue.dequeue()
        if not event:
            return None

        pipeline = EventPipeline(db)
        return pipeline.process_event(event)

    @staticmethod
    def process_all_queued(db: Session) -> List[Dict[str, Any]]:
        results = []
        pipeline = EventPipeline(db)
        while not PipelineQueue.is_empty():
            event = PipelineQueue.dequeue()
            if event:
                res = pipeline.process_event(event)
                results.append(res)
        return results
