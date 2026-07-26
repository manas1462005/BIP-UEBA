import random
import json
import datetime
from typing import List, Dict, Any
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.role import Role
from app.models.organization import Organization

PREHASHED_DUMMY_PASSWORD = "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeg6Lruj3vjPGga31lW"

FIRST_NAMES = ["Alex", "Jordan", "Taylor", "Morgan", "Sam", "Chris", "Pat", "Riley", "Casey", "Dakota", "Reese", "Quinn"]
LAST_NAMES = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez"]


class EmployeeGenerator:
    """Generates synthetic employees with realistic behavioral metadata."""

    @staticmethod
    def generate_employees(db: Session, org: Organization, config: Dict[str, Any], count: int = 50) -> List[Dict[str, Any]]:
        departments = config.get("organization", {}).get("departments", ["Engineering", "Security Operations", "HR", "Finance", "Sales"])
        offices = config.get("organization", {}).get("offices", [
            {"name": "New York HQ", "country": "United States", "city": "New York", "tz": "America/New_York"}
        ])

        roles = db.query(Role).all()
        role_map = {r.name: r.id for r in roles}
        default_role_id = role_map.get("Analyst", 2)

        employees = []
        for i in range(1, count + 1):
            fname = random.choice(FIRST_NAMES)
            lname = random.choice(LAST_NAMES)
            email = f"{fname.lower()}.{lname.lower()}{i}@bip.com"
            
            # Query existing user or create new
            user = db.query(User).filter(User.email == email).first()
            if not user:
                user = User(
                    email=email,
                    hashed_password=PREHASHED_DUMMY_PASSWORD,
                    full_name=f"{fname} {lname}",
                    role_id=role_map.get("Admin" if i == 1 else "Analyst" if i % 3 == 0 else "Viewer", default_role_id),
                    organization_id=org.id,
                    is_active=True
                )
                db.add(user)
                db.flush()

            dept = departments[i % len(departments)]
            office = offices[i % len(offices)]
            
            # Unique behavioral profile parameters for simulator
            employee_meta = {
                "user_id": user.id,
                "employee_id": f"EMP-{1000 + i}",
                "full_name": user.full_name,
                "email": user.email,
                "department": dept,
                "office": office["name"],
                "country": office["country"],
                "city": office["city"],
                "time_zone": office["tz"],
                "working_hours": f"{8 + (i % 3):02d}:00-{17 + (i % 3):02d}:00",
                "working_days": ["Mon", "Tue", "Wed", "Thu", "Fri"],
                "mfa_preference": random.choice(["TOTP", "Push Notification", "Hardware Key"]),
                "vpn_usage_pattern": random.choice(["Always", "Hybrid", "Remote-Only"]),
                "travel_frequency": random.choice(["None", "Low", "Moderate", "High"]),
                "risk_appetite": round(random.uniform(0.1, 0.9), 2)
            }
            employees.append(employee_meta)

        db.commit()
        return employees
