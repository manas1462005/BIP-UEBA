import datetime
from typing import Dict, Any, List


class EnterpriseCalendarEngine:
    """Enterprise Calendar & Schedule Simulation Engine."""

    @staticmethod
    def get_calendar_events() -> List[Dict[str, Any]]:
        return [
            {"date": "2026-01-01", "event": "New Year's Day", "type": "Public Holiday", "activity_impact": "Zero"},
            {"date": "2026-05-25", "event": "Memorial Day / Spring Holiday", "type": "Public Holiday", "activity_impact": "Zero"},
            {"date": "2026-07-04", "event": "Independence Day", "type": "Public Holiday", "activity_impact": "Zero"},
            {"date": "2026-09-15", "event": "Annual Innovation Hackathon", "type": "Company Event", "activity_impact": "High Git/Slack"},
            {"date": "2026-10-10", "event": "Q3 Infrastructure Maintenance", "type": "Maintenance Window", "activity_impact": "Off-Hours Ops"},
            {"date": "2026-11-26", "event": "Thanksgiving Day", "type": "Public Holiday", "activity_impact": "Zero"},
            {"date": "2026-12-25", "event": "Christmas Day", "type": "Company Holiday", "activity_impact": "Zero"}
        ]

    @staticmethod
    def get_day_schedule_type(sim_date: datetime.date) -> Dict[str, Any]:
        weekday = sim_date.weekday()
        if weekday in (5, 6):
            return {"schedule_type": "Weekend", "is_workday": False, "activity_factor": 0.05}
        
        # Check holiday list
        date_str = sim_date.strftime("%Y-%m-%d")
        for cal_event in EnterpriseCalendarEngine.get_calendar_events():
            if cal_event["date"] == date_str and cal_event["type"] in ("Public Holiday", "Company Holiday"):
                return {"schedule_type": cal_event["type"], "is_workday": False, "activity_factor": 0.0}

        return {"schedule_type": "Standard Weekday", "is_workday": True, "activity_factor": 1.0}
