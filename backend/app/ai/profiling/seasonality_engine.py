from typing import Dict, Any, List


class SeasonalityEngine:
    """Identifies recurring calendar patterns & seasonal behavior drivers."""

    @staticmethod
    def detect_seasonal_patterns(extracted_features: List[Dict[str, Any]]) -> Dict[str, Any]:
        has_release_weekend = any(f.get("release_weekend_activity") for f in extracted_features)
        has_weekend = any(f.get("weekend_activity") for f in extracted_features)

        return {
            "release_weekend_pattern": "Active (Off-Hours Engineering)" if has_release_weekend else "Normal",
            "month_end_financial_close": "Active for Finance & ERP Users",
            "quarter_end_review": "Increased Slack & Jira Activity",
            "public_holiday_activity": "Zero Workstation Events Expected",
            "on_call_rotation_schedule": "Bi-weekly 24/7 Coverage",
            "detected_weekend_activity": has_weekend
        }
