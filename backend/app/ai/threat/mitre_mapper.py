from typing import Dict, Any, List


class MITREMapper:
    """Maps classified threats to MITRE ATT&CK Tactics, Techniques, & Mitigations."""

    @staticmethod
    def map_mitre_attack(category: str) -> List[Dict[str, Any]]:
        if category == "Credential Compromise":
            return [
                {
                    "tactic": "Credential Access",
                    "tactic_id": "TA0006",
                    "technique_id": "T1110.003",
                    "technique_name": "Password Spraying",
                    "data_source": "DS0015 (User Account Authentication Logs)",
                    "detection_strategy": "Correlate failed authentication spikes across unique accounts from single IP range",
                    "mitigation": "M1032 (Multi-Factor Authentication)"
                },
                {
                    "tactic": "Initial Access",
                    "tactic_id": "TA0001",
                    "technique_id": "T1078.004",
                    "technique_name": "Valid Accounts: Cloud Accounts",
                    "data_source": "DS0028 (Cloud Service Authentication)",
                    "detection_strategy": "Monitor successful cloud logins following high anomaly Z-scores",
                    "mitigation": "M1018 (User Account Management)"
                }
            ]
        elif category == "Privilege Misuse":
            return [
                {
                    "tactic": "Privilege Escalation",
                    "tactic_id": "TA0004",
                    "technique_id": "T1548",
                    "technique_name": "Abuse Elevation Control Mechanism",
                    "data_source": "DS0029 (Cloud IAM Audit Logs)",
                    "detection_strategy": "Flag STS AssumeRole calls on critical production resources outside maintenance window",
                    "mitigation": "M1026 (Privileged Account Management)"
                }
            ]
        elif category == "Exfiltration":
            return [
                {
                    "tactic": "Exfiltration",
                    "tactic_id": "TA0010",
                    "technique_id": "T1041",
                    "technique_name": "Exfiltration Over C2 Channel",
                    "data_source": "DS0029 (Network Traffic Flows)",
                    "detection_strategy": "Monitor abnormal egress byte volume from database subnets",
                    "mitigation": "M1031 (Network Intrusion Prevention)"
                }
            ]
        else:
            return [
                {
                    "tactic": "Operational Normal",
                    "tactic_id": "TA0000",
                    "technique_id": "T0000",
                    "technique_name": "Benign Enterprise Activity",
                    "data_source": "DS0000 (Internal Logs)",
                    "detection_strategy": "No threat detected; verified baseline work",
                    "mitigation": "None Required"
                }
            ]
