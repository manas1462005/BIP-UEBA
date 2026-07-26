import datetime
from typing import Dict, Any, List
from app.simulator.enterprise_context.calendar_engine import EnterpriseCalendarEngine


class CalendarReasoningEngine:
    """Evaluates enterprise calendar drivers (Release Weekends, Maintenance Windows, Holidays)."""

    @staticmethod
    def evaluate_calendar(event: Dict[str, Any], profile: Dict[str, Any]) -> Dict[str, Any]:
        login_hour = float(event.get("login_hour", 9))
        is_off_hours = login_hour < 6 or login_hour > 20

        # Check seasonality / calendar driver
        seasonality = profile.get("seasonality", {})
        has_release_driver = "Active" in str(seasonality.get("release_weekend_pattern", ""))

        calendar_justified = False
        schedule_context = "Standard Weekday Work Schedule"

        if is_off_hours and has_release_driver:
            calendar_justified = True
            schedule_context = "Approved Release Weekend Deployment Window"
        elif is_off_hours and "AWS" in str(event.get("resource_accessed")):
            calendar_justified = True
            schedule_context = "Scheduled Infrastructure Maintenance Window"
        elif is_off_hours:
            schedule_context = "Unscheduled Off-Hours Activity"

        return {
            "schedule_context": schedule_context,
            "is_off_hours": is_off_hours,
            "calendar_justified": calendar_justified,
            "release_weekend_active": has_release_driver,
            "maintenance_window_active": "AWS" in str(event.get("resource_accessed"))
        }
