from fastapi import FastAPI, Body
from fastapi.responses import Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
import threading
import asyncio

from app.metrics import system_metrics, http_metrics
from app.middleware.metrics_middleware import register_middleware
from app.db import data_collection

app = FastAPI(title="FastAPI Metrics Monitoring System")

# Register middleware
register_middleware(app)

# Background task to collect system metrics
async def metrics_updater():
    while True:
        system_metrics.collect_system_metrics()
        await asyncio.sleep(5)  # collect every 5 seconds

# Start background metrics collection
threading.Thread(target=lambda: asyncio.run(metrics_updater()), daemon=True).start()

# Root endpoint
@app.get("/")
def root():
    return {"message": "FastAPI Metrics Monitoring System"}

# Health endpoint
@app.get("/health")
def health():
    return {"status": "ok"}

# Prometheus metrics endpoint
@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

# POST /data endpoint (store in MongoDB)
@app.post("/data")
async def create_data(item: dict = Body(...)):
    http_metrics.DATA_COUNT.inc()
    result = await data_collection.insert_one(item)
    return {"message": "Data added", "id": str(result.inserted_id)}

# GET /data endpoint (retrieve from MongoDB)
@app.get("/data")
async def get_data():
    data = []
    async for document in data_collection.find():
        document["_id"] = str(document["_id"])
        data.append(document)
    return data
