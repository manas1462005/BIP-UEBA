import math
from typing import List, Dict, Any


class StatisticsEngine:
    """Computes rolling averages, moving windows, variances, and frequency counts."""

    @staticmethod
    def calculate_mean(values: List[float]) -> float:
        if not values:
            return 0.0
        return sum(values) / len(values)

    @staticmethod
    def calculate_variance(values: List[float]) -> float:
        if len(values) <= 1:
            return 0.0
        mean = StatisticsEngine.calculate_mean(values)
        return sum((x - mean) ** 2 for x in values) / (len(values) - 1)

    @staticmethod
    def calculate_std_dev(values: List[float]) -> float:
        return math.sqrt(StatisticsEngine.calculate_variance(values))

    @staticmethod
    def compute_frequencies(items: List[str]) -> Dict[str, float]:
        if not items:
            return {}
        total = len(items)
        counts: Dict[str, int] = {}
        for item in items:
            counts[item] = counts.get(item, 0) + 1
        return {k: round(v / total, 4) for k, v in counts.items()}

    @staticmethod
    def compute_rolling_stats(values: List[float], window_size: int = 7) -> Dict[str, float]:
        recent = values[-window_size:] if len(values) >= window_size else values
        return {
            "rolling_mean": round(StatisticsEngine.calculate_mean(recent), 2),
            "rolling_std_dev": round(StatisticsEngine.calculate_std_dev(recent), 2),
            "sample_count": len(recent)
        }
