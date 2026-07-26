from typing import Dict, Any, List
from sqlalchemy.orm import Session
from app.models import Event
from app.ai.profiling.profile_builder import ProfileBuilder
from app.ai.profiling.profile_repository import ProfileRepository
from app.ai.profiling.version_manager import VersionManager


class ProfileManager:
    """High-level orchestrator & dependency injection container for profiling."""

    def __init__(self, db: Session):
        self.db = db

    def get_or_create_profile(self, entity_id: str, entity_type: str) -> Dict[str, Any]:
        # Query staged events from DB
        events = self.db.query(Event).filter(Event.entity_id == entity_id).all()
        raw_events = [
            {
                "event_id": e.event_id,
                "event_type": e.event_type,
                "entity_id": e.entity_id,
                "timestamp": str(e.timestamp),
                "source_ip": e.source_ip,
                "device_id": e.device_id,
                "resource_accessed": e.resource_accessed,
                "threat_label": e.threat_label
            }
            for e in events
        ]

        profile = ProfileBuilder.build_profile(entity_id, entity_type, raw_events)
        ProfileRepository.save_profile(self.db, profile)
        return profile

    def rebuild_all_profiles(self) -> Dict[str, Any]:
        # Perform full profile rebuild across enterprise entities
        user_profile = self.get_or_create_profile("user@bip.com", "user")
        dev_profile = self.get_or_create_profile("dev_1", "device")
        team_profile = self.get_or_create_profile("TEAM-ENG-01", "team")
        prj_profile = self.get_or_create_profile("PRJ-ATL-01", "project")
        bu_profile = self.get_or_create_profile("BU-CLOUD", "business_unit")
        ent_profile = self.get_or_create_profile("ENTERPRISE-01", "enterprise")

        return {
            "status": "rebuilt",
            "profiles_updated": 6,
            "sample_user_profile": user_profile
        }

    def increment_profile_version(self, entity_id: str, entity_type: str) -> Dict[str, Any]:
        profile = self.get_or_create_profile(entity_id, entity_type)
        updated_profile = VersionManager.create_version_snapshot(profile, previous_version=profile.get("version", 1))
        ProfileRepository.save_profile(self.db, updated_profile)
        return updated_profile
