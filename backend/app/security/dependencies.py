from typing import Callable, List, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.core.security import decode_access_token
from app.schemas.auth import TokenPayload

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


def get_current_user_payload(token: str = Depends(oauth2_scheme)) -> TokenPayload:
    payload_dict = decode_access_token(token)
    if not payload_dict:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return TokenPayload(**payload_dict)


def require_roles(allowed_roles: List[str]) -> Callable:
    def role_checker(payload: TokenPayload = Depends(get_current_user_payload)) -> TokenPayload:
        if not payload.role or payload.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Operation not permitted. Required role: {allowed_roles}"
            )
        return payload
    return role_checker
