from typing import Dict, Any
from fastapi import HTTPException, status
from app.core.security import create_access_token
from app.schemas.auth import LoginRequest, TokenResponse

# Mock credentials store for Phase 1 architecture verification
MOCK_USERS: Dict[str, Dict[str, Any]] = {
    "admin@bip.com": {
        "password": "Admin123!",
        "role": "Admin",
        "full_name": "System Administrator"
    },
    "analyst@bip.com": {
        "password": "Analyst123!",
        "role": "Analyst",
        "full_name": "SOC Security Analyst"
    },
    "viewer@bip.com": {
        "password": "Viewer123!",
        "role": "Viewer",
        "full_name": "Executive Viewer"
    }
}


class AuthService:
    @staticmethod
    def authenticate_mock_user(login_data: LoginRequest) -> TokenResponse:
        user = MOCK_USERS.get(login_data.username.lower())
        
        # Allow default mock login or fallback check for testing flexibility
        if not user or user["password"] != login_data.password:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
            
        token = create_access_token(
            subject=login_data.username,
            role=user["role"]
        )
        
        return TokenResponse(
            access_token=token,
            token_type="bearer",
            role=user["role"],
            user_email=login_data.username,
            user_full_name=user["full_name"]
        )
