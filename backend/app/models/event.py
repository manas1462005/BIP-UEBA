import datetime
from typing import Optional, TYPE_CHECKING
from sqlalchemy import String, Text, DateTime, ForeignKey, Float, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base_class import Base

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.device import Device


class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    event_id: Mapped[Optional[str]] = mapped_column(String(100), unique=True, index=True, nullable=True)
    event_type: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    source: Mapped[str] = mapped_column(String(100), nullable=False)

    # Entity Mapping
    entity_id: Mapped[Optional[str]] = mapped_column(String(255), index=True, nullable=True)
    entity_type: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)  # User, Device, Service Account

    # Network & Geolocation Telemetry
    source_ip: Mapped[Optional[str]] = mapped_column(String(45), nullable=True)
    country: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    city: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)

    # Host & Client Context
    device_id: Mapped[Optional[int]] = mapped_column(ForeignKey("devices.id"), nullable=True)
    device_fingerprint: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    browser: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    operating_system: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)

    # Auth & Security Context
    authentication_method: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    mfa_status: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    vpn_status: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)

    # Resource & Command Details
    resource_accessed: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    resource_sensitivity: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)  # High, Medium, Low
    session_duration: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    command_sequence: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    raw_payload: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"), nullable=True)

    timestamp: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), index=True, nullable=False
    )

    # Relationships
    user: Mapped[Optional["User"]] = relationship("User", back_populates="events")
    device: Mapped[Optional["Device"]] = relationship("Device", back_populates="events")
