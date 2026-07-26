import datetime
from typing import Optional, TYPE_CHECKING
from sqlalchemy import String, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base_class import Base

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.device import Device


class Alert(Base):
    __tablename__ = "alerts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    severity: Mapped[str] = mapped_column(String(50), nullable=False)  # Low, Medium, High, Critical
    status: Mapped[str] = mapped_column(String(50), default="Open", nullable=False)  # Open, Investigating, Resolved
    source: Mapped[str] = mapped_column(String(100), nullable=False)

    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"), nullable=True)
    device_id: Mapped[Optional[int]] = mapped_column(ForeignKey("devices.id"), nullable=True)

    timestamp: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), index=True, nullable=False
    )

    # Relationships
    user: Mapped[Optional["User"]] = relationship("User", back_populates="alerts")
    device: Mapped[Optional["Device"]] = relationship("Device", back_populates="alerts")
