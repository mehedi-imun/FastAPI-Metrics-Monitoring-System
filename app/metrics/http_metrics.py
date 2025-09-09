from prometheus_client import Counter

HTTP_REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"]
)

DATA_COUNT = Counter("data_post_total", "Total POST /data requests")
