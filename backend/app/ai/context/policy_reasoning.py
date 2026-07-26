from typing import Dict, Any, List
from app.simulator.enterprise_context.access_policy import AccessPolicyEngine


class PolicyReasoningEngine:
    """Evaluates access policies, JIT temporary grants, and RBAC compliance."""

    @staticmethod
    def evaluate_policy(event: Dict[str, Any], profile: Dict[str, Any]) -> Dict[str, Any]:
        resource = str(event.get("resource_accessed", "Azure Active Directory"))
        policies = AccessPolicyEngine.get_policies()

        matched_policy = "POL-RBAC-01 (Standard Employee Access)"
        approval_status = "Approved via Manager RBAC Assignment"
        is_jit = False

        if "AWS" in resource:
            matched_policy = "POL-JIT-03 (DevOps Production Break-Glass)"
            approval_status = "Approved via VP Engineering JIT Token"
            is_jit = True
        elif "GitHub" in resource:
            matched_policy = "POL-RBAC-02 (Developer Code Access)"
            approval_status = "Approved via Engineering RBAC Group"

        return {
            "matched_policy": matched_policy,
            "approval_status": approval_status,
            "is_jit_temporary_access": is_jit,
            "policy_compliance_state": "Compliant Policy Alignment",
            "total_active_policies_evaluated": len(policies)
        }
