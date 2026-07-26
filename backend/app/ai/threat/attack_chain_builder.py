from typing import Dict, Any, List


class AttackChainBuilder:
    """Constructs multi-stage temporal attack progression graphs."""

    @staticmethod
    def build_attack_chain(category: str, evidence: Dict[str, Any]) -> List[Dict[str, Any]]:
        if category in ("Credential Compromise", "Credential Stuffing", "Brute Force", "Privilege Misuse", "Exfiltration", "Impossible Travel", "Lateral Movement", "Device Spoofing", "Low-and-Slow Exfiltration", "Insider Drift"):
            return [
                {
                    "stage": 1,
                    "tactic": "Initial Access",
                    "technique": "T1078 (Valid Cloud Accounts)",
                    "stage_confidence": 0.90,
                    "status": "Verified Stage",
                    "details": "Successful login following anomaly trigger"
                },
                {
                    "stage": 2,
                    "tactic": "Privilege Escalation",
                    "technique": "T1548 (STS AssumeRole Elevation)",
                    "stage_confidence": 0.85,
                    "status": "Active Stage",
                    "details": "Elevated access requested on target resource"
                },
                {
                    "stage": 3,
                    "tactic": "Data Exfiltration",
                    "technique": "T1041 (Exfiltration Over Channel)",
                    "stage_confidence": 0.65,
                    "status": "Potential Progression",
                    "details": "Target resource marked for potential exfiltration"
                }
            ]
        else:
            return [
                {
                    "stage": 1,
                    "tactic": "Benign Operational Workflow",
                    "technique": "None",
                    "stage_confidence": 0.98,
                    "status": "Verified Normal",
                    "details": "Single-stage legitimate employee workday access"
                }
            ]
