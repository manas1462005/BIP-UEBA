from typing import Dict, Any, List


class RecommendationEngine:
    """Generates actionable SOC analyst recommendation checklists mapped to evidence & MITRE tactics."""

    @staticmethod
    def generate_recommendations(evidence_package: Dict[str, Any]) -> List[Dict[str, Any]]:
        category = evidence_package.get("primary_category", "Credential Compromise")
        entity_id = evidence_package.get("entity_id", "alex.smith1@bip.com")
        resource = evidence_package.get("resource_accessed", "AWS Production Console")

        if category in ("Credential Compromise", "Privilege Misuse", "Exfiltration"):
            return [
                {
                    "priority": "High",
                    "action": f"Verify user identity for {entity_id} via out-of-band communication",
                    "target": entity_id,
                    "mitre_mapping": "T1078 (Valid Accounts)",
                    "evidence_mapping": "Unmanaged Endpoint & Off-Hours Login Signal"
                },
                {
                    "priority": "High",
                    "action": "Revoke active SAML SSO sessions and force password reset",
                    "target": entity_id,
                    "mitre_mapping": "T1110.003 (Password Spraying)",
                    "evidence_mapping": "MFA Verification Failure Signal"
                },
                {
                    "priority": "Medium",
                    "action": f"Inspect AWS CloudTrail audit logs for sts:AssumeRole events on {resource}",
                    "target": resource,
                    "mitre_mapping": "T1548 (Abuse Elevation Control Mechanism)",
                    "evidence_mapping": "Production Resource Access Signal"
                },
                {
                    "priority": "Low",
                    "action": "Audit IAM policy scopes and JIT break-glass access tokens",
                    "target": "IAM Policy Engine",
                    "mitre_mapping": "M1026 (Privileged Account Management)",
                    "evidence_mapping": "Access Policy Reasoning Output"
                }
            ]
        else:
            return [
                {
                    "priority": "Low",
                    "action": "No immediate triage required; event matches verified normal operational baseline",
                    "target": entity_id,
                    "mitre_mapping": "TA0000 (Operational Normal)",
                    "evidence_mapping": "Enterprise Baseline & Calendar Justification"
                }
            ]
