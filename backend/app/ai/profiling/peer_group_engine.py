from typing import Dict, Any, List


class PeerGroupEngine:
    """Computes peer group baselines across Roles, Teams, Projects, and Locations."""

    @staticmethod
    def get_peer_group_baseline(peer_group_id: str) -> Dict[str, Any]:
        group_type = "Role Peers"
        if "TEAM" in peer_group_id:
            group_type = "Team Peers"
        elif "PRJ" in peer_group_id:
            group_type = "Project Peers"
        elif "OFFICE" in peer_group_id:
            group_type = "Regional Location Peers"

        return {
            "peer_group_id": peer_group_id,
            "peer_group_type": group_type,
            "peer_count": 12,
            "peer_typical_login_hours": [8, 9, 10],
            "peer_typical_session_duration_hours": 8.0,
            "peer_mfa_compliance_rate": 0.98,
            "peer_vpn_usage_rate": 0.85,
            "peer_top_applications": ["GitHub Enterprise", "Jira Software", "Slack", "AWS Console"],
            "peer_deviations": {
                "after_hours_login_rate": 0.04,
                "offsite_ip_access_rate": 0.02
            }
        }
