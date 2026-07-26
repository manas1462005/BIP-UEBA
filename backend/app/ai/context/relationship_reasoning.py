from typing import Dict, Any, List
from app.simulator.enterprise_context.relationship_graph import RelationshipGraphEngine


class RelationshipReasoningEngine:
    """Evaluates relationship graph distance, project assignment, and resource legitimacy."""

    @staticmethod
    def evaluate_relationships(event: Dict[str, Any], profile: Dict[str, Any]) -> Dict[str, Any]:
        entity_id = str(event.get("entity_id", "alex.smith1@bip.com"))
        resource = str(event.get("resource_accessed", "Azure Active Directory"))

        mock_emp = {
            "email": entity_id,
            "employee_id": "EMP-1001",
            "team_name": "Backend Engineering Team",
            "office": "New York HQ",
            "assigned_projects": ["Project Atlas", "Project Orion"]
        }
        graph_links = RelationshipGraphEngine.get_employee_relationships(mock_emp)

        expected_resources = ["Azure Active Directory", "GitHub Enterprise", "Jira Software", "Slack", "AWS Production Console"]
        is_expected_resource = resource in expected_resources

        rel_distance = 1.0 if is_expected_resource else 3.0
        legitimacy = "Direct Project / Role Assignment" if is_expected_resource else "Unassigned System Access"

        return {
            "relationship_distance_hops": rel_distance,
            "access_legitimacy": legitimacy,
            "assigned_projects": ["Project Atlas", "Project Orion"],
            "team_membership": "Backend Engineering Team",
            "graph_links_count": len(graph_links),
            "is_expected_resource": is_expected_resource
        }
