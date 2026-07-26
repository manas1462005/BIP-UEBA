import datetime
import random
from typing import List, Dict, Any
from sqlalchemy.orm import Session
from app.models.event import Event
from app.models.organization import Organization
from app.simulator.config import SimulatorConfig
from app.simulator.organization_generator import OrganizationGenerator
from app.simulator.employee_generator import EmployeeGenerator
from app.simulator.device_generator import DeviceGenerator
from app.simulator.resource_generator import ResourceGenerator
from app.simulator.normal_behavior_simulator import NormalBehaviorSimulator
from app.simulator.behavioral_drift_engine import BehavioralDriftEngine
from app.simulator.attack_campaign_generator import AttackCampaignGenerator


class TelemetryEngine:
    """Orchestrates Digital Twin generation and stores telemetry into PostgreSQL."""

    def __init__(self, db: Session, config: SimulatorConfig = None):
        self.db = db
        self.config = (config or SimulatorConfig.get_default()).config

    def run_simulation(self, days: int = 1, inject_attacks: bool = True) -> List[Dict[str, Any]]:
        # 1. Generate Organization
        org = OrganizationGenerator.generate_organization(self.db, self.config)

        # 2. Generate Employees & Devices
        num_emp = self.config.get("simulation_parameters", {}).get("num_employees", 20)
        employees = EmployeeGenerator.generate_employees(self.db, org, self.config, count=num_emp)
        devices = DeviceGenerator.generate_devices(self.db, org, employees)
        resources = ResourceGenerator.generate_resources()

        device_by_user = {d["user_id"]: d for d in devices}

        all_events = []
        start_date = datetime.date.today() - datetime.timedelta(days=days)

        # 3. Simulate Daily Events
        for day_offset in range(days):
            current_date = start_date + datetime.timedelta(days=day_offset)

            for emp in employees:
                # Apply behavioral drift over time
                emp_drifted = BehavioralDriftEngine.apply_monthly_drift(emp, day_offset)
                dev = device_by_user.get(emp["user_id"], devices[0])

                # Normal behavior telemetry
                emp_events = NormalBehaviorSimulator.generate_daily_events_for_employee(
                    emp_drifted, dev, resources, current_date
                )
                all_events.extend(emp_events)

            # Inject Attack Campaigns
            if inject_attacks and (day_offset == days - 1 or random.random() < 0.15):
                target_emp = random.choice(employees)
                target_dev = device_by_user.get(target_emp["user_id"], devices[0])
                attack_start = datetime.datetime.combine(current_date, datetime.time(14, 0, 0))
                
                attack_events = AttackCampaignGenerator.inject_attack_campaign(
                    target_emp, target_dev, resources, attack_start
                )
                all_events.extend(attack_events)

        # 4. Save events into PostgreSQL
        for evt_data in all_events:
            event_obj = Event(
                event_id=evt_data.get("event_id"),
                event_type=evt_data.get("event_type", "security.event"),
                source=evt_data.get("source", "TelemetryEngine"),
                entity_id=evt_data.get("entity_id"),
                entity_type=evt_data.get("entity_type"),
                source_ip=evt_data.get("source_ip"),
                country=evt_data.get("country"),
                city=evt_data.get("city"),
                device_id=evt_data.get("device_id"),
                device_fingerprint=evt_data.get("device_fingerprint"),
                browser=evt_data.get("browser"),
                operating_system=evt_data.get("operating_system"),
                authentication_method=evt_data.get("authentication_method"),
                mfa_status=evt_data.get("mfa_status"),
                vpn_status=evt_data.get("vpn_status"),
                resource_accessed=evt_data.get("resource_accessed"),
                resource_sensitivity=evt_data.get("resource_sensitivity"),
                session_duration=evt_data.get("session_duration"),
                command_sequence=evt_data.get("command_sequence"),
                raw_payload=evt_data.get("trust_signals"),
                user_id=evt_data.get("user_id"),
                timestamp=evt_data.get("timestamp")
            )
            self.db.add(event_obj)

        self.db.commit()
        return all_events
