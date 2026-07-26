from typing import Dict, Any


class MaturityEngine:
    """Tracks profile maturity lifecycle transitions."""

    STATES = ["New", "Learning", "Growing", "Stable", "Trusted", "Archived"]

    @staticmethod
    def determine_maturity(sample_count: int, confidence_score: float) -> str:
        if sample_count < 5:
            return "New"
        elif sample_count < 20:
            return "Learning"
        elif sample_count < 50:
            return "Growing"
        elif confidence_score < 0.85:
            return "Stable"
        else:
            return "Trusted"
