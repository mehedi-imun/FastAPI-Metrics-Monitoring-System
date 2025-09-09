import time
from fastapi import Request
from app.metrics.http_metrics import HTTP_REQUEST_COUNT

def register_middleware(app):
    @app.middleware("http")
    async def metrics_middleware(request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)

        # Increment Prometheus counter
        HTTP_REQUEST_COUNT.labels(
            method=request.method,
            endpoint=request.url.path,
            status=response.status_code
        ).inc()

        return response
