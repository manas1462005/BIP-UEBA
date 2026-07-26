from typing import Dict, Any, List
from sqlalchemy.orm import Session
from app.models.organization import Organization
from app.models.role import Role


class OrganizationGenerator:
    """Generates enterprise structure, roles, and organizational metadata."""

    @staticmethod
    def generate_organization(db: Session, config: Dict[str, Any]) -> Organization:
        org_name = config.get("organization", {}).get("name", "Global CyberTech Enterprise")
        
        # Query or create organization
        org = db.query(Organization).filter(Organization.name == org_name).first()
        if not org:
            org = Organization(name=org_name)
            db.add(org)
            db.commit()
            db.refresh(org)

        # Seed standard RBAC roles if missing
        default_roles = [
            ("Admin", "Full platform administration access"),
            ("Analyst", "Security operations triage access"),
            ("Viewer", "Read-only executive dashboard access")
        ]
        for role_name, desc in default_roles:
            role = db.query(Role).filter(Role.name == role_name).first()
            if not role:
                db.add(Role(name=role_name, description=desc))
        db.commit()

        return org

    @staticmethod
    def get_departments(config: Dict[str, Any]) -> List[str]:
        return config.get("organization", {}).get(
            "departments",
            ["Engineering", "Security Operations", "Human Resources", "Finance", "Executive Leadership", "Sales"]
        )

    @staticmethod
    def get_offices(config: Dict[str, Any]) -> List[Dict[str, str]]:
        return config.get("organization", {}).get("offices", [
            {"name": "New York HQ", "country": "United States", "city": "New York", "tz": "America/New_York"}
        ])
