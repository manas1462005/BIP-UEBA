import random
import uuid
from typing import List, Dict, Any
from sqlalchemy.orm import Session
from app.models.device import Device
from app.models.organization import Organization


DEVICE_TYPES = [
    ("MacBook Pro 16", "macOS Sonoma 14.4", "Safari 17.4"),
    ("ThinkPad X1 Carbon", "Windows 11 Enterprise", "Chrome 123.0"),
    ("Dell Latitude 5540", "Windows 11 Pro", "Edge 123.0"),
    ("Ubuntu Workstation", "Ubuntu 22.04 LTS", "Firefox 124.0"),
    ("Virtual Desktop VM", "Windows Server 2022", "Chrome 122.0"),
    ("Corporate iPhone 15", "iOS 17.4", "Mobile Safari"),
]


class DeviceGenerator:
    """Generates synthetic enterprise devices linked to employees."""

    @staticmethod
    def generate_devices(db: Session, org: Organization, employees: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        devices_list = []

        for emp in employees:
            dev_type, os_name, browser_name = random.choice(DEVICE_TYPES)
            hostname = f"{emp['department'].lower()[:3]}-{emp['employee_id'].lower()}-dev"
            
            # Query existing device or create new
            device = db.query(Device).filter(Device.hostname == hostname).first()
            if not device:
                ip_suffix = random.randint(10, 250)
                device = Device(
                    hostname=hostname,
                    ip_address=f"10.100.{random.randint(1, 20)}.{ip_suffix}",
                    mac_address=f"00:50:56:{random.randint(10,99):02x}:{random.randint(10,99):02x}:{random.randint(10,99):02x}",
                    os=os_name,
                    is_active=True,
                    organization_id=org.id
                )
                db.add(device)
                db.flush()

            device_meta = {
                "device_id": device.id,
                "hostname": device.hostname,
                "ip_address": device.ip_address,
                "mac_address": device.mac_address,
                "os": os_name,
                "browser": browser_name,
                "device_fingerprint": f"fp_{uuid.uuid4().hex[:12]}",
                "user_id": emp["user_id"],
                "owner_email": emp["email"],
                "patch_level": random.choice(["Up-to-date", "Pending Minor", "Outdated"]),
                "is_corporate_managed": True
            }
            devices_list.append(device_meta)

        db.commit()
        return devices_list
