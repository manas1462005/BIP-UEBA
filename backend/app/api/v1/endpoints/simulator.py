from typing import Optional
from fastapi import APIRouter, Depends, Query, Response, status
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.simulator.telemetry_engine import TelemetryEngine
from app.simulator.exporter import TelemetryExporter

router = APIRouter()


@router.post(
    "/simulator/generate",
    status_code=status.HTTP_200_OK,
    summary="Trigger Digital Twin Telemetry Simulation",
    description="Generates synthetic enterprise telemetry events and persists them into PostgreSQL."
)
def generate_telemetry(
    days: int = Query(1, ge=1, le=365, description="Number of simulation days to generate"),
    inject_attacks: bool = Query(True, description="Whether to inject cyber attack campaign chains"),
    db: Session = Depends(get_db)
):
    engine = TelemetryEngine(db)
    events = engine.run_simulation(days=days, inject_attacks=inject_attacks)
    return {
        "status": "success",
        "days_generated": days,
        "events_count": len(events),
        "sample_event": events[0] if events else None
    }


@router.get(
    "/simulator/export",
    summary="Export Synthetic Telemetry Data",
    description="Exports generated telemetry data in CSV, JSON, or Parquet format."
)
def export_telemetry(
    format: str = Query("json", regex="^(csv|json|parquet)$"),
    days: int = Query(1, ge=1, le=365),
    db: Session = Depends(get_db)
):
    engine = TelemetryEngine(db)
    events = engine.run_simulation(days=days, inject_attacks=False)

    if format == "csv":
        data = TelemetryExporter.export_to_csv(events)
        return Response(content=data, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=telemetry.csv"})
    elif format == "parquet":
        data = TelemetryExporter.export_to_parquet(events)
        return Response(content=data, media_type="application/octet-stream", headers={"Content-Disposition": "attachment; filename=telemetry.parquet"})
    else:
        data = TelemetryExporter.export_to_json(events)
        return Response(content=data, media_type="application/json", headers={"Content-Disposition": "attachment; filename=telemetry.json"})


@router.get(
    "/simulator/status",
    summary="Digital Twin Status & Statistics",
    description="Returns high-level statistics of generated enterprise entities."
)
def get_simulator_status(db: Session = Depends(get_db)):
    from app.models.user import User
    from app.models.device import Device
    from app.models.event import Event
    
    user_count = db.query(User).count()
    device_count = db.query(Device).count()
    event_count = db.query(Event).count()

    return {
        "status": "active",
        "total_employees": user_count,
        "total_devices": device_count,
        "total_events_in_db": event_count
    }
