from typing import List, Dict, Any


class RelationshipGraphEngine:
    """Generates queryable relational graph links stored in PostgreSQL metadata."""

    @staticmethod
    def get_employee_relationships(employee: Dict[str, Any]) -> List[Dict[str, str]]:
        emp_email = employee.get("email", "operator@bip.com")
        emp_id = employee.get("employee_id", "EMP-1001")

        return [
            {"source": emp_email, "relationship": "REPORTS_TO", "target": employee.get("manager_email", "admin@bip.com")},
            {"source": emp_email, "relationship": "MEMBER_OF_TEAM", "target": employee.get("team_name", "Backend Engineering Team")},
            {"source": emp_email, "relationship": "ASSIGNED_TO_PROJECT", "target": employee.get("assigned_projects", ["Project Atlas"])[0]},
            {"source": emp_email, "relationship": "OWNS_DEVICE", "target": f"{emp_id.lower()}-dev"},
            {"source": emp_email, "relationship": "BASED_IN_OFFICE", "target": employee.get("office", "New York HQ")},
            {"source": emp_email, "relationship": "CONNECTS_VIA_NETWORK", "target": "Corporate Office LAN"},
            {"source": f"{emp_id.lower()}-dev", "relationship": "CONNECTED_TO", "target": "Corporate Office LAN"},
            {"source": "GitHub Enterprise", "relationship": "DEPENDS_ON_DB", "target": "Customer Data Postgres DB"},
            {"source": "Project Atlas", "relationship": "REQUIRES_RESOURCE", "target": "GitHub Enterprise"}
        ]
