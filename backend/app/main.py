from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.core.config import settings
from app.core.logging import setup_logging, logger
from app.database.session import engine
from app.models import Base
from app.api.v1.api import api_router
from app.schemas.health import HealthResponse

# Initialize structured logging
setup_logging()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup Lifespan: Auto-create tables for local execution/testing if needed
    logger.info("Initializing Behavioral Intelligence Platform Backend Architecture...")
    logger.info(f"Environment: {settings.ENVIRONMENT}")
    logger.info(f"CORS Origins: {settings.CORS_ORIGINS}")
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        logger.warning(f"Metadata create_all check: {e}")
    yield
    # Shutdown Lifespan
    logger.info("Shutting down Behavioral Intelligence Platform Backend Architecture...")


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url=f"{settings.API_V1_STR}/docs",
    redoc_url=f"{settings.API_V1_STR}/redoc",
    lifespan=lifespan
)

# CORS Configuration
if settings.CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


# Global Exception Handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Global Exception caught at {request.url.path}: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "An internal server error occurred.", "path": str(request.url.path)}
    )


# Direct /health endpoint for root queries & Docker health check
@app.get(
    "/health",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
    tags=["Health"],
    summary="Root Health Endpoint"
)
def root_health():
    return HealthResponse(status="healthy")


# Include API v1 Router (/api/v1)
app.include_router(api_router, prefix=settings.API_V1_STR)
