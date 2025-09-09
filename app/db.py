from motor.motor_asyncio import AsyncIOMotorClient

# Update the MongoDB URI if needed
MONGO_DETAILS = "mongodb+srv://apollo-gear:apollo-gear@cluster0.v6dfbfz.mongodb.net/metricsWithPy?retryWrites=true&w=majority&appName=Cluster0"

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.fastapi_metrics
data_collection = database.get_collection("data")
