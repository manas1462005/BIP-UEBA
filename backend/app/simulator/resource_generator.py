from typing import List, Dict, Any

RESOURCES = [
    {"name": "GitHub Enterprise", "category": "Code Repository", "sensitivity": "High", "permission": "Developer"},
    {"name": "Jira Issue Tracker", "category": "Project Management", "sensitivity": "Medium", "permission": "User"},
    {"name": "Slack Workspace", "category": "Communication", "sensitivity": "Low", "permission": "Employee"},
    {"name": "Corporate Email (Exchange)", "category": "Communication", "sensitivity": "Medium", "permission": "Employee"},
    {"name": "Workday HR Portal", "category": "Human Resources", "sensitivity": "High", "permission": "HR/Employee"},
    {"name": "Payroll ERP System", "category": "Finance", "sensitivity": "Critical", "permission": "Finance Admin"},
    {"name": "AWS Production Console", "category": "Cloud Infrastructure", "sensitivity": "Critical", "permission": "DevOps/Admin"},
    {"name": "Azure Active Directory", "category": "Identity Provider", "sensitivity": "Critical", "permission": "Global Admin"},
    {"name": "Corporate VPN Gateway", "category": "Network Gateway", "sensitivity": "High", "permission": "Employee"},
    {"name": "Customer Data Postgres DB", "category": "Database", "sensitivity": "Critical", "permission": "DBA/Backend"},
    {"name": "Salesforce CRM", "category": "Sales", "sensitivity": "High", "permission": "Sales/Support"},
]


class ResourceGenerator:
    """Generates synthetic enterprise application resources."""

    @staticmethod
    def generate_resources() -> List[Dict[str, Any]]:
        return RESOURCES
