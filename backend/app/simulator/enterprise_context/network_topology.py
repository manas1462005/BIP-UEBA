from typing import List, Dict, Any


NETWORK_TOPOLOGY = [
    {
        "zone": "Corporate Office LAN",
        "subnet": "10.100.0.0/16",
        "description": "Internal wired & secure wireless corporate workstations",
        "security_level": "Trusted"
    },
    {
        "zone": "Corporate VPN Gateway",
        "subnet": "10.200.0.0/16",
        "description": "Encrypted remote access gateway for remote employees",
        "security_level": "Enforced MFA"
    },
    {
        "zone": "Production Subnet",
        "subnet": "172.16.10.0/24",
        "description": "Production application servers and core customer workloads",
        "security_level": "Restricted / Critical"
    },
    {
        "zone": "Development & Staging Subnet",
        "subnet": "172.16.20.0/24",
        "description": "Engineer testing environments and build servers",
        "security_level": "Internal Dev"
    },
    {
        "zone": "DMZ (Demilitarized Zone)",
        "subnet": "192.168.1.0/24",
        "description": "Public facing web gateways, reverse proxies, and API endpoints",
        "security_level": "Exposed DMZ"
    },
    {
        "zone": "Database Cluster Subnet",
        "subnet": "172.16.30.0/24",
        "description": "Isolated database servers and encrypted storage arrays",
        "security_level": "Isolated Critical"
    },
    {
        "zone": "Identity & Auth Servers",
        "subnet": "10.100.5.0/24",
        "description": "Active Directory domain controllers and SAML/OAuth IdP",
        "security_level": "High Security"
    }
]


class NetworkTopologyEngine:
    """Generates enterprise network topology metadata."""

    @staticmethod
    def get_topology() -> List[Dict[str, Any]]:
        return NETWORK_TOPOLOGY
