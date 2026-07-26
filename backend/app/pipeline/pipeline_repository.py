import time
from typing import Dict, Any, List


class PipelineRepository:
    """Repository for tracking pipeline execution metrics, stage timings, & queue status."""

    _EVENTS_PROCESSED_COUNT: int = 0
    _FAILED_EVENTS_COUNT: int = 0
    _RETRY_COUNT: int = 0
    _STAGE_TIMINGS: Dict[str, List[float]] = {
        "feature_extraction": [],
        "behaviour_profiling": [],
        "anomaly_detection": [],
        "context_reasoning": [],
        "threat_classification": [],
        "explainability_generation": []
    }
    _RECENT_PIPELINE_LOGS: List[Dict[str, Any]] = []

    @staticmethod
    def record_stage_timing(stage_name: str, timing_ms: float) -> None:
        if stage_name in PipelineRepository._STAGE_TIMINGS:
            PipelineRepository._STAGE_TIMINGS[stage_name].append(timing_ms)
            if len(PipelineRepository._STAGE_TIMINGS[stage_name]) > 200:
                PipelineRepository._STAGE_TIMINGS[stage_name].pop(0)

    @staticmethod
    def record_event_processed(log_entry: Dict[str, Any]) -> None:
        PipelineRepository._EVENTS_PROCESSED_COUNT += 1
        PipelineRepository._RECENT_PIPELINE_LOGS.append(log_entry)
        if len(PipelineRepository._RECENT_PIPELINE_LOGS) > 300:
            PipelineRepository._RECENT_PIPELINE_LOGS.pop(0)

    @staticmethod
    def record_failed_event() -> None:
        PipelineRepository._FAILED_EVENTS_COUNT += 1

    @staticmethod
    def get_metrics() -> Dict[str, Any]:
        avg_stage_timings = {}
        total_avg_latency = 0.0

        for stage, timings in PipelineRepository._STAGE_TIMINGS.items():
            if timings:
                avg = sum(timings) / len(timings)
                avg_stage_timings[stage] = round(avg, 2)
                total_avg_latency += avg
            else:
                avg_stage_timings[stage] = 0.50
                total_avg_latency += 0.50

        total_processed = max(PipelineRepository._EVENTS_PROCESSED_COUNT, 1)
        success_rate = round(((total_processed - PipelineRepository._FAILED_EVENTS_COUNT) / total_processed) * 100, 1)

        return {
            "pipeline_status": "Active / Live",
            "events_processed": total_processed,
            "failed_events": PipelineRepository._FAILED_EVENTS_COUNT,
            "retry_count": PipelineRepository._RETRY_COUNT,
            "success_rate_percent": success_rate,
            "average_total_latency_ms": round(total_avg_latency, 2),
            "stage_timings_ms": avg_stage_timings,
            "recent_logs": PipelineRepository._RECENT_PIPELINE_LOGS[-20:]
        }
