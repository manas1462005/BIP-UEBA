import datetime
from typing import Optional
from sqlalchemy import String, Float, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base_class import Base


class RiskScore(Base):
    __tablename__ = "riskscores"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    entity_type: Mapped[str] = mapped_column(String(50), nullable=False)  # User, Device, IP, Session
    entity_id: Mapped[str] = mapped_column(String(255), index=True, nullable=False)

    # Multi-Dimensional Sub-Scores
    behaviour_score: Mapped[Optional[float]] = mapped_column(Float, nullable=True, default=0.0)
    trust_score: Mapped[Optional[float]] = mapped_column(Float, nullable=True, default=100.0)
    context_score: Mapped[Optional[float]] = mapped_column(Float, nullable=True, default=0.0)
    threat_score: Mapped[Optional[float]] = mapped_column(Float, nullable=True, default=0.0)

    # Composite Score & Metrics
    final_risk_score: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    confidence: Mapped[Optional[float]] = mapped_column(Float, nullable=True, default=1.0)
    risk_level: Mapped[Optional[str]] = mapped_column(String(50), nullable=True, default="Low")  # Low, Medium, High, Critical

    calculation_timestamp: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
