import os
from typing import Dict, Any

DEFAULT_CONFIG: Dict[str, Any] = {
    "organization": {
        "name": "Global CyberTech Enterprise",
        "industry": "Cybersecurity & Technology Solutions",
        "countries": ["United States", "United Kingdom", "Germany", "Singapore"],
        "offices": [
            {"name": "New York HQ", "country": "United States", "city": "New York", "tz": "America/New_York"},
            {"name": "London Regional Office", "country": "United Kingdom", "city": "London", "tz": "Europe/London"},
            {"name": "Berlin Hub", "country": "Germany", "city": "Berlin", "tz": "Europe/Berlin"},
            {"name": "Singapore Hub", "country": "Singapore", "city": "Singapore", "tz": "Asia/Singapore"}
        ],
        "departments": ["Engineering", "Security Operations", "Human Resources", "Finance", "Executive Leadership", "Sales"]
    },
    "simulation_parameters": {
        "num_employees": 50,
        "remote_work_percentage": 0.35,
        "travel_frequency_percentage": 0.15,
        "attack_campaign_rate": 0.05,
        "business_hours": {"start_hour": 9, "end_hour": 17}
    }
}


class SimulatorConfig:
    def __init__(self, config_dict: Dict[str, Any] = None):
        self.config = config_dict or DEFAULT_CONFIG

    @classmethod
    def get_default(cls) -> "SimulatorConfig":
        return cls(DEFAULT_CONFIG)
