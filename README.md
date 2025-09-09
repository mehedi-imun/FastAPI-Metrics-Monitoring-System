# FastAPI Metrics Monitoring System

## Project Overview

A FastAPI application that provides system-level and application-level metrics monitoring in Prometheus format. Tracks CPU, memory, and HTTP request metrics while storing sample data in MongoDB.

---

## Features

* Monitors CPU and memory usage
* Tracks HTTP requests (counts, response statuses)
* Prometheus-compatible `/metrics` endpoint
* MongoDB integration for storing/retrieving sample data
* Fully asynchronous and high-performance

---

## Endpoints

| Method | Path       | Description                              |
| ------ | ---------- | ---------------------------------------- |
| GET    | `/`        | Root endpoint, returns a welcome message |
| GET    | `/health`  | Health check, returns `ok`               |
| GET    | `/metrics` | Prometheus metrics for monitoring        |
| POST   | `/data`    | Store sample data in MongoDB             |
| GET    | `/data`    | Retrieve all stored data from MongoDB    |

---

## Setup & Run

1. **Install dependencies**

```bash
pip install -r requirements.txt
```

2. **Configure MongoDB**
   Update `app/db.py` with your MongoDB URI.

3. **Run the app**

```bash
uvicorn app.main:app --reload
```

---

## Usage

Open in browser or via Postman/curl:

* Root: `http://127.0.0.1:8000/`
* Health: `http://127.0.0.1:8000/health`
* Metrics: `http://127.0.0.1:8000/metrics`
* POST /data example:

```json
{
  "name": "Test Item",
  "value": 123
}
```

---

## Highlights

* Asynchronous, production-ready FastAPI app
* Prometheus-compatible metrics for monitoring
* Persistent MongoDB storage for sample data
* Easy to extend with additional metrics or endpoints

---

## Future Enhancements

* Request duration histograms and 95th percentile latency
* Request/response size tracking
* Additional system metrics: uptime, thread count, GC stats

