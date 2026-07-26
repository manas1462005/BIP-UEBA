import json
from typing import Optional, Dict, Any
from sqlalchemy.orm import Session
from app.models import BehaviourProfile
from app.ai.profiling.profile_builder import ProfileBuilder


class ProfileRepository:
    """PostgreSQL database persistence interface for behavioral profiles."""

    @staticmethod
    def get_profile(db: Session, entity_id: str, entity_type: str) -> Dict[str, Any]:
        db_profile = db.query(BehaviourProfile).filter(
            BehaviourProfile.entity_id == entity_id,
            BehaviourProfile.entity_type == entity_type
        ).first()

        if db_profile and db_profile.profile_data_json:
            try:
                return json.loads(db_profile.profile_data_json)
            except Exception:
                pass

        # Generate on-demand fallback profile
        return ProfileBuilder.build_profile(entity_id, entity_type, [])

    @staticmethod
    def save_profile(db: Session, profile_data: Dict[str, Any]) -> BehaviourProfile:
        entity_id = profile_data.get("entity_id", "user@bip.com")
        entity_type = profile_data.get("entity_type", "user")
        json_str = json.dumps(profile_data)

        db_profile = db.query(BehaviourProfile).filter(
            BehaviourProfile.entity_id == entity_id,
            BehaviourProfile.entity_type == entity_type
        ).first()

        if not db_profile:
            db_profile = BehaviourProfile(
                entity_id=entity_id,
                entity_type=entity_type,
                profile_data_json=json_str
            )
            db.add(db_profile)
        else:
            db_profile.profile_data_json = json_str

        db.commit()
        db.refresh(db_profile)
        return db_profile
