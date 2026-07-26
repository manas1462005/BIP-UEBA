import time
import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import Response

logger = logging.getLogger("bip.middleware")


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """Middleware to log request duration and status codes."""

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        start_time = time.time()
        response = await call_next(request)
        process_time = (time.time() - start_time) * 1000
        
        logger.info(
            "%s %s - Status: %d - Process Time: %.2fms",
            request.method,
            request.url.path,
            response.status_code,
            process_time
        )
        response.headers["X-Process-Time"] = f"{process_time:.2f}ms"
        return response
