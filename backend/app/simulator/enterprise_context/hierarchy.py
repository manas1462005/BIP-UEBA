import random
from typing import List, Dict, Any

BUSINESS_UNITS = [
    "Cloud & Infrastructure Services",
    "Enterprise Software Solutions",
    "Global Security Operations",
    "Corporate Financial Services"
]

PROJECTS_CATALOG = [
    {
        "project_id": "PRJ-ATL-01",
        "name": "Project Atlas",
        "business_unit": "Enterprise Software Solutions",
        "sensitivity": "High",
        "tech_stack": "Python, React, PostgreSQL",
        "criticality": "Mission Critical"
    },
    {
        "project_id": "PRJ-ORN-02",
        "name": "Project Orion",
        "business_unit": "Cloud & Infrastructure Services",
        "sensitivity": "Critical",
        "tech_stack": "AWS, Kubernetes, Terraform",
        "criticality": "Mission Critical"
    },
    {
        "project_id": "PRJ-FLC-03",
        "name": "Project Falcon",
        "business_unit": "Global Security Operations",
        "sensitivity": "High",
        "tech_stack": "Go, ElasticSearch, Kafka",
        "criticality": "High"
    },
    {
        "project_id": "PRJ-CLM-04",
        "name": "Cloud Migration",
        "business_unit": "Cloud & Infrastructure Services",
        "sensitivity": "Medium",
        "tech_stack": "Azure, Docker, Ansible",
        "criticality": "High"
    },
    {
        "project_id": "PRJ-ERP-05",
        "name": "ERP Modernisation",
        "business_unit": "Corporate Financial Services",
        "sensitivity": "Critical",
        "tech_stack": "SAP, Oracle DB, Java",
        "criticality": "Mission Critical"
    },
    {
        "project_id": "PRJ-SOC-06",
        "name": "Security Operations",
        "business_unit": "Global Security Operations",
        "sensitivity": "Critical",
        "tech_stack": "Python, SIEM, SOAR",
        "criticality": "Mission Critical"
    },
    {
        "project_id": "PRJ-AIP-07",
        "name": "AI Platform",
        "business_unit": "Enterprise Software Solutions",
        "sensitivity": "High",
        "tech_stack": "PyTorch, FastAPI, VectorDB",
        "criticality": "High"
    }
]


class HierarchyEngine:
    """Generates organizational hierarchy and project assignments."""

    @staticmethod
    def get_projects() -> List[Dict[str, Any]]:
        return PROJECTS_CATALOG

    @staticmethod
    def get_teams() -> List[Dict[str, Any]]:
        return [
            {"team_id": "TEAM-ENG-01", "name": "Backend Engineering Team", "department": "Engineering"},
            {"team_id": "TEAM-ENG-02", "name": "Frontend Platform Team", "department": "Engineering"},
            {"team_id": "TEAM-SOC-01", "name": "SOC Threat Response", "department": "Security Operations"},
            {"team_id": "TEAM-HR-01", "name": "People Operations", "department": "Human Resources"},
            {"team_id": "TEAM-FIN-01", "name": "Financial Analytics", "department": "Finance"}
        ]

    @staticmethod
    def assign_hierarchy_to_employee(emp: Dict[str, Any], index: int) -> Dict[str, Any]:
        bu = BUSINESS_UNITS[index % len(BUSINESS_UNITS)]
        team = HierarchyEngine.get_teams()[index % len(HierarchyEngine.get_teams())]
        assigned_projects = random.sample(PROJECTS_CATALOG, k=random.randint(1, 2))

        emp["business_unit"] = bu
        emp["team_name"] = team["name"]
        emp["team_id"] = team["team_id"]
        emp["manager_email"] = "admin@bip.com" if index > 0 else "board@bip.com"
        emp["assigned_projects"] = [p["name"] for p in assigned_projects]
        emp["project_ids"] = [p["project_id"] for p in assigned_projects]

        return emp
