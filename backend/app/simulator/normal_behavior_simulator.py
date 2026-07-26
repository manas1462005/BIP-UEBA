import random
import datetime
import uuid
from typing import List, Dict, Any


class NormalBehaviorSimulator:
    """Generates realistic daily employee events based on role and schedule."""

    @staticmethod
    def generate_daily_events_for_employee(
        employee: Dict[str, Any],
        device: Dict[str, Any],
        resources: List[Dict[str, Any]],
        sim_date: datetime.date
    ) -> List[Dict[str, Any]]:
        # Skip weekends for standard schedules
        if sim_date.weekday() in (5, 6) and random.random() > 0.1:
            return []

        events = []
        user_id = employee["user_id"]
        dev_id = device["device_id"]
        
        # 1. Login Event at Start of Workday
        start_hour = int(employee["working_hours"].split(":")[0])
        login_time = datetime.datetime.combine(
            sim_date,
            datetime.time(start_hour, random.randint(0, 20), random.randint(0, 59))
        )

        session_id = f"sess_{uuid.uuid4().hex[:10]}"
        
        # Determine VPN requirement
        uses_vpn = employee["vpn_usage_pattern"] in ("Always", "Remote-Only")
        
        events.append({
            "event_id": f"evt_{uuid.uuid4().hex[:12]}",
            "timestamp": login_time,
            "event_type": "user.login",
            "source": "IdentityManager",
            "entity_id": employee["email"],
            "entity_type": "User",
            "department": employee["department"],
            "role": "Analyst",
            "office": employee["office"],
            "country": employee["country"],
            "city": employee["city"],
            "source_ip": device["ip_address"],
            "user_id": user_id,
            "device_id": dev_id,
            "device_fingerprint": device["device_fingerprint"],
            "operating_system": device["os"],
            "browser": device["browser"],
            "authentication_method": employee["mfa_preference"],
            "mfa_status": "Passed",
            "vpn_status": "Connected" if uses_vpn else "Direct",
            "resource_accessed": "Azure Active Directory",
            "resource_sensitivity": "Critical",
            "command_sequence": "AUTHENTICATE_SESSION",
            "session_duration": 0.0,
            "trust_signals": json_dumps({"mfa_verified": True, "known_device": True, "trusted_ip": True}),
            "threat_label": "Benign"
        })

        # 2. Application Access Events throughout the Workday
        current_time = login_time + datetime.timedelta(minutes=random.randint(5, 15))
        dept_apps = [r for r in resources if r["category"] in ("Communication", "Project Management", "Code Repository")]

        for _ in range(random.randint(4, 8)):
            current_time += datetime.timedelta(minutes=random.randint(30, 90))
            if current_time.hour >= 18:
                break
                
            app = random.choice(dept_apps if dept_apps else resources)
            events.append({
                "event_id": f"evt_{uuid.uuid4().hex[:12]}",
                "timestamp": current_time,
                "event_type": "resource.access",
                "source": app["name"],
                "entity_id": employee["email"],
                "entity_type": "User",
                "department": employee["department"],
                "role": "Analyst",
                "office": employee["office"],
                "country": employee["country"],
                "city": employee["city"],
                "source_ip": device["ip_address"],
                "user_id": user_id,
                "device_id": dev_id,
                "device_fingerprint": device["device_fingerprint"],
                "operating_system": device["os"],
                "browser": device["browser"],
                "authentication_method": "SSO_OAuth2",
                "mfa_status": "Valid",
                "vpn_status": "Connected" if uses_vpn else "Direct",
                "resource_accessed": app["name"],
                "resource_sensitivity": app["sensitivity"],
                "command_sequence": f"READ_{app['name'].upper()}",
                "session_duration": float(random.randint(15, 60)),
                "trust_signals": json_dumps({"mfa_verified": True, "known_device": True}),
                "threat_label": "Benign"
            })

        # 3. Logout Event
        logout_time = datetime.datetime.combine(
            sim_date,
            datetime.time(17, random.randint(0, 30), random.randint(0, 59))
        )
        events.append({
            "event_id": f"evt_{uuid.uuid4().hex[:12]}",
            "timestamp": logout_time,
            "event_type": "user.logout",
            "source": "IdentityManager",
            "entity_id": employee["email"],
            "entity_type": "User",
            "department": employee["department"],
            "role": "Analyst",
            "office": employee["office"],
            "country": employee["country"],
            "city": employee["city"],
            "source_ip": device["ip_address"],
            "user_id": user_id,
            "device_id": dev_id,
            "device_fingerprint": device["device_fingerprint"],
            "operating_system": device["os"],
            "browser": device["browser"],
            "authentication_method": "SessionTerminated",
            "mfa_status": "None",
            "vpn_status": "Disconnected",
            "resource_accessed": "SessionGateway",
            "resource_sensitivity": "Low",
            "command_sequence": "LOGOUT_CLEAN",
            "session_duration": float((logout_time - login_time).seconds // 60),
            "trust_signals": json_dumps({"clean_logout": True}),
            "threat_label": "Benign"
        })

        return events


def json_dumps(obj: Any) -> str:
    import json
    return json.dumps(obj)
