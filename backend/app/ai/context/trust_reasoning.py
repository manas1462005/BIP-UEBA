from typing import Dict, Any, List


class TrustReasoningEngine:
    """Evaluates device compliance, network trust, and authentication strength."""

    @staticmethod
    def evaluate_trust(event: Dict[str, Any], profile: Dict[str, Any]) -> Dict[str, Any]:
        device_id = str(event.get("device_id", "dev_1001"))
        vpn_used = bool(event.get("vpn_used", False))
        mfa_verified = bool(event.get("mfa_verified", True))
        source_ip = str(event.get("source_ip", "10.100.4.12"))

        known_ips = profile.get("baseline", {}).get("known_ips", ["10.100.4.12"])
        is_known_ip = source_ip in known_ips or "10.100" in source_ip or "10.200" in source_ip
        is_managed_device = "dev" in device_id.lower() or "laptop" in device_id.lower() or "mac" in device_id.lower()

        trust_level = "High Trust"
        mitigating_factors: List[str] = []
        concerning_factors: List[str] = []

        if is_managed_device:
            mitigating_factors.append("Managed Corporate Hardware (Compliant Patch State)")
        else:
            concerning_factors.append("Unmanaged / Personal Hardware Detected")

        if mfa_verified:
            mitigating_factors.append("Enforced SAML2.0 + MFA Success")
        else:
            concerning_factors.append("MFA Verification Missing / Bypassed")

        if vpn_used or is_known_ip:
            mitigating_factors.append("Authenticated Encrypted Corporate Network Gateway")
        else:
            concerning_factors.append("Untrusted External Public IP Subnet")

        if len(concerning_factors) >= 2:
            trust_level = "Untrusted Access Context"
        elif len(concerning_factors) == 1:
            trust_level = "Medium Trust (Partial Mitigations)"

        return {
            "trust_level": trust_level,
            "trust_confidence": 0.95 if is_managed_device else 0.70,
            "is_managed_device": is_managed_device,
            "is_known_ip": is_known_ip,
            "mfa_verified": mfa_verified,
            "mitigating_factors": mitigating_factors,
            "concerning_factors": concerning_factors
        }
