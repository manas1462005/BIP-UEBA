from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base_class import Base


class ThreatType(Base):
    __tablename__ = "threattypes"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    category: Mapped[str] = mapped_column(String(100), nullable=False)  # Insider Threat, Anomaly, External Attack
    mitre_tactic: Mapped[str] = mapped_column(String(100), nullable=True)  # e.g., T1059, TA0001
    description: Mapped[str] = mapped_column(Text, nullable=True)
