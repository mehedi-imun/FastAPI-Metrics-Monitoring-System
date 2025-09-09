# app/db.py
import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get MongoDB URI from environment
MONGO_DETAILS = os.getenv("MONGO_DETAILS")

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.fastapi_metrics
data_collection = database.get_collection("data")
