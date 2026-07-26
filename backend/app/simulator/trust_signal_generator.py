import json
import random
from typing import Dict, Any


class TrustSignalGenerator:
    """Generates telemetry trust context indicators."""

    @staticmethod
    def generate_trust_context(is_anomalous: bool = False) -> Dict[str, Any]:
        if not is_anomalous:
            return {
                "mfa_verified": True,
                "known_device": True,
                "corporate_vpn": True,
                "trusted_ip": True,
                "device_compliance": "Compliant",
                "session_approval": "Approved"
            }
        else:
            return {
                "mfa_verified": random.choice([True, False]),
                "known_device": False,
                "corporate_vpn": False,
                "trusted_ip": False,
                "device_compliance": random.choice(["Non-Compliant", "Unknown"]),
                "session_approval": "Pending_Review"
            }
