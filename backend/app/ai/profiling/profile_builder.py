from typing import List, Dict, Any
from app.ai.profiling.feature_extractor import FeatureExtractor
from app.ai.profiling.baseline_engine import BaselineEngine
from app.ai.profiling.confidence_engine import ConfidenceEngine
from app.ai.profiling.maturity_engine import MaturityEngine
from app.ai.profiling.seasonality_engine import SeasonalityEngine
from app.ai.profiling.peer_group_engine import PeerGroupEngine


class ProfileBuilder:
    """Synthesizes hierarchical profiles & non-ML Behavior Fingerprints."""

    @staticmethod
    def build_fingerprint(baseline: Dict[str, Any], features: List[Dict[str, Any]]) -> Dict[str, Any]:
        return {
            "working_style": "Standard Enterprise Hours (09:00 - 17:00)",
            "authentication_behaviour": "SAML2.0 + Enforced Okta MFA",
            "application_usage": list(baseline.get("application_frequencies", {}).keys()),
            "resource_access": ["Azure AD", "GitHub Enterprise", "Jira Software", "Slack"],
            "device_usage": baseline.get("known_devices", ["dev_1"]),
            "travel_behaviour": "Low / Domestic Only",
            "network_usage": "Corporate LAN & Enforced VPN Gateway",
            "typical_session_pattern": "Single long continuous workday session",
            "relationship_pattern": "Direct team collaboration with Manager & Peers",
            "project_participation": ["Project Atlas", "Project Orion"]
        }

    @staticmethod
    def build_profile(entity_id: str, entity_type: str, raw_events: List[Dict[str, Any]]) -> Dict[str, Any]:
        extracted = [FeatureExtractor.extract_features(e) for e in raw_events] if raw_events else []
        baseline = BaselineEngine.generate_baseline(extracted)
        confidence = ConfidenceEngine.calculate_confidence(extracted)
        maturity = MaturityEngine.determine_maturity(len(extracted), confidence["confidence_score"])
        seasonality = SeasonalityEngine.detect_seasonal_patterns(extracted)
        peer_baseline = PeerGroupEngine.get_peer_group_baseline(f"PEER-{entity_type.upper()}")
        fingerprint = ProfileBuilder.build_fingerprint(baseline, extracted)

        return {
            "entity_id": entity_id,
            "entity_type": entity_type,
            "version": 1,
            "maturity_state": maturity,
            "confidence": confidence,
            "baseline": baseline,
            "behavior_fingerprint": fingerprint,
            "peer_group_baseline": peer_baseline,
            "seasonality": seasonality,
            "historical_versions": [
                {"version": 1, "created_at": "2026-07-25T12:00:00Z", "maturity": maturity}
            ]
        }
