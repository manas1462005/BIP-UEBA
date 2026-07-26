from typing import Dict, Any


class BusinessCriticalityEngine:
    """Weights resource sensitivity, system importance, & business impact."""

    @staticmethod
    def evaluate_criticality(event: Dict[str, Any], profile: Dict[str, Any]) -> Dict[str, Any]:
        resource = str(event.get("resource_accessed", "Azure Active Directory"))

        if "AWS" in resource or "DB" in resource or "Payroll" in resource:
            sensitivity = "Critical"
            impact = "Mission Critical (Core Customer Workloads / Financial Data)"
            multiplier = 1.5
        elif "GitHub" in resource or "Jira" in resource:
            sensitivity = "High"
            impact = "High Impact (Proprietary Source Code & IP)"
            multiplier = 1.2
        else:
            sensitivity = "Medium"
            impact = "Moderate Operational Impact"
            multiplier = 1.0

        return {
            "resource_sensitivity": sensitivity,
            "business_impact": impact,
            "contextual_risk_multiplier": multiplier,
            "data_classification": "Confidential / Restricted" if sensitivity in ("High", "Critical") else "Internal"
        }
