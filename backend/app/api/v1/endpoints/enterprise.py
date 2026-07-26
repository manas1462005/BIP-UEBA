from typing import Optional
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.simulator.enterprise_context.hierarchy import HierarchyEngine
from app.simulator.enterprise_context.calendar_engine import EnterpriseCalendarEngine
from app.simulator.enterprise_context.network_topology import NetworkTopologyEngine
from app.simulator.enterprise_context.access_policy import AccessPolicyEngine
from app.simulator.enterprise_context.relationship_graph import RelationshipGraphEngine

router = APIRouter()


@router.get(
    "/enterprise",
    status_code=status.HTTP_200_OK,
    summary="Enterprise Organizational Metadata",
    description="Returns high-level business units, departments, and offices."
)
def get_enterprise_metadata():
    return {
        "organization": "Global CyberTech Enterprise",
        "business_units": [
            "Cloud & Infrastructure Services",
            "Enterprise Software Solutions",
            "Global Security Operations",
            "Corporate Financial Services"
        ],
        "departments": ["Engineering", "Security Operations", "Human Resources", "Finance", "Sales"],
        "offices": [
            {"name": "New York HQ", "country": "United States", "city": "New York"},
            {"name": "London Regional Office", "country": "United Kingdom", "city": "London"},
            {"name": "Berlin Hub", "country": "Germany", "city": "Berlin"},
            {"name": "Singapore Hub", "country": "Singapore", "city": "Singapore"}
        ]
    }


@router.get(
    "/projects",
    status_code=status.HTTP_200_OK,
    summary="Enterprise Projects Catalog"
)
def get_projects():
    return {"projects": HierarchyEngine.get_projects()}


@router.get(
    "/teams",
    status_code=status.HTTP_200_OK,
    summary="Enterprise Teams Directory"
)
def get_teams():
    return {"teams": HierarchyEngine.get_teams()}


@router.get(
    "/network",
    status_code=status.HTTP_200_OK,
    summary="Enterprise Infrastructure & Network Topology"
)
def get_network():
    return {"topology": NetworkTopologyEngine.get_topology()}


@router.get(
    "/policies",
    status_code=status.HTTP_200_OK,
    summary="Enterprise Access Control Policies"
)
def get_policies():
    return {"policies": AccessPolicyEngine.get_policies()}


@router.get(
    "/relationships/{employee_id}",
    status_code=status.HTTP_200_OK,
    summary="Employee Relational Graph Links"
)
def get_employee_relationships(employee_id: str):
    mock_emp = {
        "email": f"{employee_id.lower()}@bip.com",
        "employee_id": employee_id,
        "team_name": "Backend Engineering Team",
        "office": "New York HQ",
        "assigned_projects": ["Project Atlas"]
    }
    return {
        "employee_id": employee_id,
        "relationships": RelationshipGraphEngine.get_employee_relationships(mock_emp)
    }


@router.get(
    "/calendar",
    status_code=status.HTTP_200_OK,
    summary="Enterprise Calendar Events"
)
def get_calendar():
    return {"calendar_events": EnterpriseCalendarEngine.get_calendar_events()}
