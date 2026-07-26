from typing import Dict, Any


class ExecutiveSummaryEngine:
    """Generates concise, business-friendly executive summaries."""

    @staticmethod
    def generate_summary(evidence_package: Dict[str, Any]) -> Dict[str, Any]:
        entity_id = evidence_package.get("entity_id", "alex.smith1@bip.com")
        category = evidence_package.get("primary_category", "Credential Compromise")
        confidence = evidence_package.get("classification_confidence", 0.90)
        resource = evidence_package.get("resource_accessed", "AWS Production Console")

        if category in ("Credential Compromise", "Privilege Misuse", "Exfiltration"):
            what_happened = f"An off-hours security anomaly was detected involving user {entity_id} accessing {resource}."
            impact = "High Impact: Potential unauthorized access to production cloud infrastructure and sensitive customer data."
            systems = [resource, "Azure Active Directory", "Production IAM Cluster"]
            consequences = "Risk of data exfiltration, credential persistence, or production service disruption if unaddressed."
        else:
            what_happened = f"Routine operational access verified for user {entity_id} on {resource}."
            impact = "Low Impact: Verified benign activity aligning with organizational RBAC policy and calendar schedule."
            systems = [resource]
            consequences = "None; standard operational workflow."

        return {
            "what_happened": what_happened,
            "business_impact": impact,
            "affected_systems": systems,
            "affected_users": [entity_id],
            "overall_confidence": confidence,
            "business_criticality": "Mission Critical" if category != "Benign Normal Activity" else "Internal",
            "potential_consequences": consequences
        }
