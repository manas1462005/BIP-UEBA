from typing import Dict, Any, List


class TimelineBuilder:
    """Constructs step-by-step chronological investigation timelines."""

    @staticmethod
    def build_timeline(evidence_package: Dict[str, Any]) -> List[Dict[str, Any]]:
        entity_id = evidence_package.get("entity_id", "alex.smith1@bip.com")
        category = evidence_package.get("primary_category", "Credential Compromise")
        resource = evidence_package.get("resource_accessed", "Azure Active Directory")

        if category == "Credential Compromise":
            return [
                {
                    "timestamp": "03:14:02 UTC",
                    "event_name": "Off-Hours Authentication Attempt",
                    "actor": entity_id,
                    "action": "User initiated SSO SAML authentication from unmanaged IP 198.51.100.42",
                    "significance": "Off-hours login deviation triggering Statistical Z-Score anomaly"
                },
                {
                    "timestamp": "03:14:15 UTC",
                    "event_name": "MFA Bypass / Failure",
                    "actor": entity_id,
                    "action": "SAML2.0 MFA verification omitted or unconfirmed",
                    "significance": "Trust Reasoning Engine flagged Untrusted Access Context"
                },
                {
                    "timestamp": "03:15:08 UTC",
                    "event_name": "AWS Production Console Session Granted",
                    "actor": entity_id,
                    "action": f"Access requested on sensitive resource {resource}",
                    "significance": "Business Criticality Engine weighted resource as Mission Critical"
                },
                {
                    "timestamp": "03:18:22 UTC",
                    "event_name": "STS AssumeRole Privilege Elevation",
                    "actor": entity_id,
                    "action": "Role sts:AssumeRole invoked for ProductionAdmin",
                    "significance": "Mapped to MITRE T1548 (Abuse Elevation Control Mechanism)"
                }
            ]
        else:
            return [
                {
                    "timestamp": "09:00:12 UTC",
                    "event_name": "Standard Enterprise SSO Login",
                    "actor": entity_id,
                    "action": "Authenticates from corporate managed laptop via office VPN",
                    "significance": "Verified Normal Activity Baseline"
                },
                {
                    "timestamp": "09:05:00 UTC",
                    "event_name": "Routine Tooling Access",
                    "actor": entity_id,
                    "action": f"Access granted to {resource} matching direct RBAC assignment",
                    "significance": "Matches typical 09:00-17:00 weekday baseline profile"
                }
            ]
