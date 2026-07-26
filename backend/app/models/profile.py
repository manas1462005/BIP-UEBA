import datetime
from typing import Optional
from sqlalchemy import String, Text, Float, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base_class import Base


class BehaviourProfile(Base):
    __tablename__ = "behaviourprofiles"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    entity_type: Mapped[str] = mapped_column(String(50), nullable=False)  # User, Device, Network
    entity_id: Mapped[str] = mapped_column(String(255), index=True, nullable=False)

    # Baseline Attributes (Stored as JSON / Text structures)
    typical_login_hours: Mapped[Optional[str]] = mapped_column(Text, nullable=True)  # e.g., JSON array of active hour bins
    typical_working_days: Mapped[Optional[str]] = mapped_column(Text, nullable=True)  # e.g., JSON array of weekdays
    known_devices: Mapped[Optional[str]] = mapped_column(Text, nullable=True)        # JSON list of device fingerprints
    known_countries: Mapped[Optional[str]] = mapped_column(Text, nullable=True)      # JSON list of country codes
    known_cities: Mapped[Optional[str]] = mapped_column(Text, nullable=True)         # JSON list of cities
    known_resources: Mapped[Optional[str]] = mapped_column(Text, nullable=True)      # JSON list of high-value targets

    # Baseline Statistics
    avg_session_duration: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    auth_preferences: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # AI Model & Embedding References
    behaviour_embedding_ref: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    # Scoring & Risk Trends
    trust_score: Mapped[Optional[float]] = mapped_column(Float, nullable=True, default=100.0)
    risk_trend: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)  # Increasing, Decreasing, Stable

    profile_data_json: Mapped[Optional[str]] = mapped_column(Text, nullable=True)  # Legacy/Flexible payload dump

    last_baseline_update: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )
