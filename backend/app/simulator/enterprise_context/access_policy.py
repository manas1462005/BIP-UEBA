from typing import List, Dict, Any

POLICIES = [
    {
        "policy_id": "POL-RBAC-01",
        "name": "Standard Employee Access",
        "type": "Role Based Access Control",
        "resource": "Slack & Email",
        "approval_required": "Automatic",
        "expiry": "Indefinite"
    },
    {
        "policy_id": "POL-RBAC-02",
        "name": "Developer Code Access",
        "type": "Role Based Access Control",
        "resource": "GitHub Enterprise",
        "approval_required": "Manager Approval",
        "expiry": "1 Year"
    },
    {
        "policy_id": "POL-JIT-03",
        "name": "DevOps Production Break-Glass",
        "type": "Privileged Temporary Access",
        "resource": "AWS Production Console",
        "approval_required": "VP Engineering Approval",
        "expiry": "4 Hours"
    },
    {
        "policy_id": "POL-FIN-04",
        "name": "Payroll ERP Access",
        "type": "Role Based Access Control",
        "resource": "Payroll ERP System",
        "approval_required": "CFO Approval",
        "expiry": "Indefinite"
    }
]


class AccessPolicyEngine:
    """Generates enterprise security access policies."""

    @staticmethod
    def get_policies() -> List[Dict[str, Any]]:
        return POLICIES
