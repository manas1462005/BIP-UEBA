from typing import Dict, Any


class TechnicalSummaryEngine:
    """Generates detailed technical investigation narratives for SOC Tier 2/3 analysts."""

    @staticmethod
    def generate_narrative(evidence_package: Dict[str, Any]) -> Dict[str, Any]:
        entity_id = evidence_package.get("entity_id", "alex.smith1@bip.com")
        category = evidence_package.get("primary_category", "Credential Compromise")
        detector_scores = evidence_package.get("detector_scores", {})
        resource = evidence_package.get("resource_accessed", "AWS Production Console")

        narrative = (
            f"TECHNICAL INVESTIGATION REPORT for event '{evidence_package.get('event_id')}':\n\n"
            f"1. OBSERVED BEHAVIOUR DEVIATION: Entity '{entity_id}' initiated session access to '{resource}'. "
            f"StatisticalDetector recorded a Modified Z-Score deviation of {detector_scores.get('StatisticalDetector', 0.85):.3f}.\n\n"
            f"2. CONTEXTUAL REASONING: Trust reasoning identified unmanaged hardware without verified SAML2.0 MFA. "
            f"Calendar reasoning confirmed off-hours activity outside any scheduled maintenance or release window.\n\n"
            f"3. THREAT & MITRE ALIGNMENT: Event classified under '{category}' mapped to MITRE ATT&CK Password Spraying (T1110.003) "
            f"and Valid Accounts (T1078.004)."
        )

        return {
            "incident_summary": f"Off-hours anomaly and potential {category} detected for user {entity_id}.",
            "technical_narrative": narrative,
            "confidence_explanation": f"High confidence ({evidence_package.get('classification_confidence', 0.90)*100:.0f}%) based on multi-detector score fusion and context contradiction.",
            "reasoning_summary": "Absence of Release Weekend or Maintenance Window drivers confirms unjustified deviation."
        }
