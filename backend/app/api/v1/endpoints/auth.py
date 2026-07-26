from fastapi import APIRouter, status
from app.schemas.auth import LoginRequest, TokenResponse
from app.services.auth_service import AuthService

router = APIRouter()


@router.post(
    "/auth/login",
    response_model=TokenResponse,
    status_code=status.HTTP_200_OK,
    summary="Mock Login & JWT Token Generation",
    description="Authenticates user credentials and returns signed JWT access token with role claims."
)
def login(login_data: LoginRequest) -> TokenResponse:
    return AuthService.authenticate_mock_user(login_data)
