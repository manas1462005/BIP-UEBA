import datetime
from typing import List, Optional, TYPE_CHECKING
from sqlalchemy import String, Boolean, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base_class import Base

if TYPE_CHECKING:
    from app.models.organization import Organization
    from app.models.event import Event
    from app.models.alert import Alert


class Device(Base):
    __tablename__ = "devices"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    hostname: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    ip_address: Mapped[str] = mapped_column(String(45), nullable=False)  # IPv4 / IPv6
    mac_address: Mapped[Optional[str]] = mapped_column(String(17), nullable=True)
    os: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    organization_id: Mapped[Optional[int]] = mapped_column(ForeignKey("organizations.id"), nullable=True)

    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    # Relationships
    organization: Mapped[Optional["Organization"]] = relationship("Organization", back_populates="devices")
    events: Mapped[List["Event"]] = relationship("Event", back_populates="device")
    alerts: Mapped[List["Alert"]] = relationship("Alert", back_populates="device")
