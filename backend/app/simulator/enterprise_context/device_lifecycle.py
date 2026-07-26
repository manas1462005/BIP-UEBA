import random
from typing import List, Dict, Any

LIFECYCLE_STATES = ["Purchased", "Provisioned", "Assigned", "Patched", "Maintenance", "Reassigned", "Retired"]


class DeviceLifecycleEngine:
    """Generates lifecycle metadata for enterprise devices."""

    @staticmethod
    def get_device_lifecycle(device_id: int) -> Dict[str, Any]:
        state = LIFECYCLE_STATES[min(device_id % len(LIFECYCLE_STATES), 3)]  # Most devices active
        age_months = random.randint(3, 36)
        
        return {
            "device_id": device_id,
            "lifecycle_state": state,
            "device_age_months": age_months,
            "firmware_version": f"v2.{random.randint(1, 9)}.{random.randint(0, 99)}",
            "compliance_state": "Compliant" if state in ("Assigned", "Patched") else "Pending Review",
            "patch_history": [
                {"patch_id": "KB503412", "installed_at": "2026-01-15", "status": "Success"},
                {"patch_id": "KB503522", "installed_at": "2026-02-20", "status": "Success"}
            ],
            "warranty_months_remaining": max(0, 36 - age_months)
        }
