from typing import Dict, Any, List


class FeaturePipeline:
    """Standardized feature vector preparation pipeline for detectors."""

    @staticmethod
    def prepare_vector(event: Dict[str, Any], profile: Dict[str, Any]) -> Dict[str, Any]:
        login_hour = float(event.get("login_hour", 9))
        session_duration = float(event.get("session_duration_minutes", 480))
        is_vpn = 1.0 if event.get("vpn_used", False) else 0.0
        is_mfa = 1.0 if event.get("mfa_verified", True) else 0.0
        
        sensitivity = event.get("resource_sensitivity", "Medium")
        sens_map = {"Low": 1.0, "Medium": 2.0, "High": 3.0, "Critical": 4.0}
        sens_score = float(sens_map.get(sensitivity, 2.0))

        return {
            "login_hour": login_hour,
            "session_duration_minutes": session_duration,
            "vpn_used": is_vpn,
            "mfa_verified": is_mfa,
            "resource_sensitivity_num": sens_score,
            "raw_event": event,
            "profile": profile
        }
