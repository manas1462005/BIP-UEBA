import random
from typing import Dict, Any


class BehavioralDriftEngine:
    """Simulates behavioral drift and lifecycle events for employees over time."""

    @staticmethod
    def apply_monthly_drift(employee: Dict[str, Any], day_of_year: int) -> Dict[str, Any]:
        # Drift triggers every 60 days for a subset of employees
        if day_of_year % 60 == 0 and random.random() < 0.2:
            events = ["Travel", "Promotion", "New_Laptop", "Relocation"]
            drift_type = random.choice(events)

            if drift_type == "Travel":
                employee["country"] = random.choice(["United Kingdom", "Germany", "Japan"])
                employee["city"] = random.choice(["London", "Berlin", "Tokyo"])
                employee["travel_frequency"] = "High"
            elif drift_type == "Promotion":
                employee["risk_appetite"] = min(1.0, employee["risk_appetite"] + 0.1)
            elif drift_type == "New_Laptop":
                employee["vpn_usage_pattern"] = "Always"

        return employee
