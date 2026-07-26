from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.ai.profiling.profile_manager import ProfileManager
from app.ai.profiling.peer_group_engine import PeerGroupEngine

router = APIRouter()


@router.get("/users/{user_id}", status_code=status.HTTP_200_OK)
def get_user_profile(user_id: str, db: Session = Depends(get_db)):
    mgr = ProfileManager(db)
    return mgr.get_or_create_profile(user_id, "user")


@router.get("/devices/{device_id}", status_code=status.HTTP_200_OK)
def get_device_profile(device_id: str, db: Session = Depends(get_db)):
    mgr = ProfileManager(db)
    return mgr.get_or_create_profile(device_id, "device")


@router.get("/teams/{team_id}", status_code=status.HTTP_200_OK)
def get_team_profile(team_id: str, db: Session = Depends(get_db)):
    mgr = ProfileManager(db)
    return mgr.get_or_create_profile(team_id, "team")


@router.get("/projects/{project_id}", status_code=status.HTTP_200_OK)
def get_project_profile(project_id: str, db: Session = Depends(get_db)):
    mgr = ProfileManager(db)
    return mgr.get_or_create_profile(project_id, "project")


@router.get("/departments/{dept_id}", status_code=status.HTTP_200_OK)
def get_department_profile(dept_id: str, db: Session = Depends(get_db)):
    mgr = ProfileManager(db)
    return mgr.get_or_create_profile(dept_id, "department")


@router.get("/business-units/{bu_id}", status_code=status.HTTP_200_OK)
def get_business_unit_profile(bu_id: str, db: Session = Depends(get_db)):
    mgr = ProfileManager(db)
    return mgr.get_or_create_profile(bu_id, "business_unit")


@router.get("/enterprise", status_code=status.HTTP_200_OK)
def get_enterprise_profile(db: Session = Depends(get_db)):
    mgr = ProfileManager(db)
    return mgr.get_or_create_profile("ENTERPRISE-01", "enterprise")


@router.get("/peer-group/{peer_id}", status_code=status.HTTP_200_OK)
def get_peer_group_profile(peer_id: str):
    return PeerGroupEngine.get_peer_group_baseline(peer_id)


@router.post("/rebuild", status_code=status.HTTP_200_OK)
def rebuild_profiles(db: Session = Depends(get_db)):
    mgr = ProfileManager(db)
    return mgr.rebuild_all_profiles()


@router.post("/update", status_code=status.HTTP_200_OK)
def update_profile(entity_id: str = "user@bip.com", entity_type: str = "user", db: Session = Depends(get_db)):
    mgr = ProfileManager(db)
    return mgr.get_or_create_profile(entity_id, entity_type)


@router.post("/version", status_code=status.HTTP_200_OK)
def version_profile(entity_id: str = "user@bip.com", entity_type: str = "user", db: Session = Depends(get_db)):
    mgr = ProfileManager(db)
    return mgr.increment_profile_version(entity_id, entity_type)
