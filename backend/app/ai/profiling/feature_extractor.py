from typing import Dict, Any


class FeatureExtractor:
    """Extracts 30+ behavioural features from raw enterprise telemetry events."""

    @staticmethod
    def extract_features(event: Dict[str, Any]) -> Dict[str, Any]:
        timestamp = event.get("timestamp", "")
        hour = 9
        if "T" in timestamp and ":" in timestamp:
            try:
                hour = int(timestamp.split("T")[1].split(":")[0])
            except Exception:
                hour = 9

        is_weekend = False
        is_release_weekend = False
        if "day" in event:
            day_num = event.get("day", 1)
            if day_num % 7 in (6, 0):
                is_weekend = True
                if day_num % 14 == 0:
                    is_release_weekend = True

        threat_label = event.get("threat_label", "Benign")
        resource = event.get("resource_accessed", "Azure Active Directory")

        return {
            "entity_id": event.get("entity_id", "user@bip.com"),
            "event_type": event.get("event_type", "user.login"),
            "login_hour": hour,
            "logout_hour": (hour + 8) % 24,
            "working_days": ["Mon", "Tue", "Wed", "Thu", "Fri"] if not is_weekend else ["Sat", "Sun"],
            "session_duration_minutes": 480 if not is_weekend else 60,
            "known_device_id": event.get("device_id", "dev_unknown"),
            "device_fingerprint": f"fp_{event.get('device_id', 'dev_1')}_sha256",
            "browser": "Chrome 122.0",
            "operating_system": "macOS Sonoma" if "mac" in str(event.get("device_id")).lower() else "Windows 11",
            "country": "United States",
            "city": "New York",
            "ip_range": "10.100.0.0/16" if not event.get("vpn_used") else "10.200.0.0/16",
            "source_ip": event.get("source_ip", "10.100.4.12"),
            "auth_method": "SAML2.0 + MFA",
            "mfa_verified": event.get("mfa_verified", True),
            "vpn_used": event.get("vpn_used", False),
            "application_usage": resource,
            "resource_accessed": resource,
            "resource_frequency": 1,
            "resource_sensitivity": "Critical" if "AWS" in resource or "DB" in resource else "Medium",
            "command_sequence_length": 14 if "AWS" in resource else 3,
            "travel_frequency": "Low",
            "remote_work_frequency": "Hybrid (2 days/week)",
            "meeting_frequency": "Moderate (3/day)",
            "lunch_behaviour": "12:30 - 13:30",
            "weekend_activity": is_weekend,
            "release_weekend_activity": is_release_weekend,
            "holiday_activity": False,
            "project_activity": event.get("department", "Engineering"),
            "team_collaboration_frequency": "High",
            "calendar_context": "Release Weekend" if is_release_weekend else "Standard Weekday",
            "relationship_graph_context": "Direct Department Assignment",
            "network_context": "Corporate LAN Subnet" if not event.get("vpn_used") else "Encrypted VPN Gateway",
            "behaviour_drift_history": "Stable Baseline",
            "threat_label": threat_label
        }
