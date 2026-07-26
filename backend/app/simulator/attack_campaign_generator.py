import random
import datetime
import json
import uuid
from typing import List, Dict, Any

ATTACK_TYPES = [
    "Brute Force",
    "Impossible Travel",
    "Credential Stuffing",
    "Lateral Movement",
    "Device Spoofing",
    "Low-and-Slow Exfiltration",
    "Insider Drift",
    "Edge Case"
]


class AttackCampaignGenerator:
    """Generates multi-stage cyber attack scenarios matching the exact assignment taxonomy."""

    @staticmethod
    def inject_attack_campaign(
        target_employee: Dict[str, Any],
        target_device: Dict[str, Any],
        resources: List[Dict[str, Any]],
        start_time: datetime.datetime = None,
        specific_scenario: str = None
    ) -> List[Dict[str, Any]]:
        campaign_type = specific_scenario if specific_scenario in ATTACK_TYPES else random.choice(ATTACK_TYPES)
        events = []

        user_id = target_employee.get("user_id", "usr_001")
        dev_id = target_device.get("device_id", "dev_001")
        t = start_time if start_time is not None else datetime.datetime.now()
        target_email = target_employee.get("email", "alex.smith1@bip.com")
        department = target_employee.get("department", "Engineering")

        geo_loc = {
            "country": "Foreign Country",
            "city": "Unknown",
            "latitude": 48.8566,
            "longitude": 2.3522
        }

        if campaign_type == "Brute Force":
            for i in range(5):
                t += datetime.timedelta(seconds=10)
                events.append({
                    "event_id": f"evt_bf_{uuid.uuid4().hex[:8]}",
                    "timestamp": t,
                    "event_type": "auth.failed",
                    "source": "IdentityManager",
                    "entity_id": target_email,
                    "entity_type": "User",
                    "department": department,
                    "source_ip": "198.51.100.42",
                    "geo_location": json.dumps(geo_loc),
                    "country": geo_loc["country"],
                    "city": geo_loc["city"],
                    "user_id": user_id,
                    "device_id": dev_id,
                    "device_fingerprint": "fp_unknown_unmanaged",
                    "authentication_method": "Password",
                    "resource_accessed": "Azure Active Directory",
                    "command_sequence": f"AUTH_FAIL_{i+1}",
                    "session_duration": 0.0,
                    "trust_signals": json.dumps({"mfa_verified": False}),
                    "threat_label": "Brute Force"
                })

        elif campaign_type == "Impossible Travel":
            events.append({
                "event_id": f"evt_it_1_{uuid.uuid4().hex[:8]}",
                "timestamp": t,
                "event_type": "user.login",
                "source": "IdentityManager",
                "entity_id": target_email,
                "entity_type": "User",
                "department": department,
                "source_ip": "198.51.100.1",
                "geo_location": json.dumps({"country": "United States", "city": "New York"}),
                "country": "United States",
                "city": "New York",
                "user_id": user_id,
                "device_id": dev_id,
                "device_fingerprint": target_device.get("fingerprint", "fp_managed_corp"),
                "authentication_method": "SAML_SSO",
                "resource_accessed": "Jira Corporate",
                "command_sequence": "LOGIN_SUCCESS",
                "session_duration": 120.0,
                "trust_signals": json.dumps({"mfa_verified": True}),
                "threat_label": "Normal Baseline"
            })
            t += datetime.timedelta(minutes=15)
            events.append({
                "event_id": f"evt_it_2_{uuid.uuid4().hex[:8]}",
                "timestamp": t,
                "event_type": "user.login",
                "source": "IdentityManager",
                "entity_id": target_email,
                "entity_type": "User",
                "department": department,
                "source_ip": "203.0.113.88",
                "geo_location": json.dumps({"country": "Japan", "city": "Tokyo"}),
                "country": "Japan",
                "city": "Tokyo",
                "user_id": user_id,
                "device_id": dev_id,
                "device_fingerprint": "fp_spoofed_japan",
                "authentication_method": "Password",
                "resource_accessed": "AWS Production Console",
                "command_sequence": "IMPOSSIBLE_TRAVEL_LOGIN",
                "session_duration": 15.0,
                "trust_signals": json.dumps({"mfa_verified": False}),
                "threat_label": "Impossible Travel"
            })

        elif campaign_type == "Credential Stuffing":
            for _ in range(3):
                t += datetime.timedelta(seconds=15)
                events.append({
                    "event_id": f"evt_cs_{uuid.uuid4().hex[:8]}",
                    "timestamp": t,
                    "event_type": "auth.failed",
                    "source": "IdentityManager",
                    "entity_id": target_email,
                    "entity_type": "User",
                    "department": department,
                    "source_ip": "185.220.101.5",
                    "geo_location": json.dumps(geo_loc),
                    "country": geo_loc["country"],
                    "city": geo_loc["city"],
                    "user_id": user_id,
                    "device_id": dev_id,
                    "device_fingerprint": "fp_stuffing_bot",
                    "authentication_method": "StolenCredentials",
                    "resource_accessed": "Azure Active Directory",
                    "command_sequence": "STUFFING_ATTEMPT",
                    "session_duration": 0.0,
                    "trust_signals": json.dumps({"mfa_verified": False}),
                    "threat_label": "Credential Stuffing"
                })

        else:
            events.append({
                "event_id": f"evt_ec_{uuid.uuid4().hex[:8]}",
                "timestamp": t,
                "event_type": "system.maintenance",
                "source": "CloudTrail",
                "entity_id": target_email,
                "entity_type": "User",
                "department": department,
                "source_ip": "10.100.4.1",
                "geo_location": json.dumps({"country": "United States", "city": "New York"}),
                "country": "United States",
                "city": "New York",
                "user_id": user_id,
                "device_id": dev_id,
                "device_fingerprint": target_device.get("fingerprint", "fp_managed_corp"),
                "authentication_method": "API_Key",
                "resource_accessed": "AWS Infrastructure",
                "command_sequence": "MAINTENANCE_SCRIPT_RUN",
                "session_duration": 15.0,
                "trust_signals": json.dumps({"mfa_verified": True, "maintenance_window": True}),
                "threat_label": "Normal Baseline"
            })

        return events
