from typing import List, Dict, Any
from app.ai.profiling.statistics_engine import StatisticsEngine


class BaselineEngine:
    """Generates baseline temporal & resource distributions for an entity."""

    @staticmethod
    def generate_baseline(extracted_features: List[Dict[str, Any]]) -> Dict[str, Any]:
        if not extracted_features:
            return {
                "typical_login_hours": [8, 9, 10],
                "typical_working_days": ["Mon", "Tue", "Wed", "Thu", "Fri"],
                "known_devices": ["dev_1"],
                "known_ips": ["10.100.4.12"],
                "application_frequencies": {"Azure Active Directory": 1.0}
            }

        hours = [f.get("login_hour", 9) for f in extracted_features]
        ips = [f.get("source_ip", "10.100.4.12") for f in extracted_features]
        devices = [f.get("known_device_id", "dev_1") for f in extracted_features]
        apps = [f.get("application_usage", "Azure Active Directory") for f in extracted_features]

        mean_hour = StatisticsEngine.calculate_mean(hours)
        std_hour = StatisticsEngine.calculate_std_dev(hours)

        return {
            "typical_login_hours": [max(0, int(mean_hour - 1)), int(mean_hour), min(23, int(mean_hour + 1))],
            "hour_mean": round(mean_hour, 2),
            "hour_std_dev": round(std_hour, 2),
            "typical_working_days": ["Mon", "Tue", "Wed", "Thu", "Fri"],
            "known_devices": list(set(devices)),
            "known_ips": list(set(ips)),
            "application_frequencies": StatisticsEngine.compute_frequencies(apps)
        }
