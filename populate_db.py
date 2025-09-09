import asyncio
from app.db import data_collection

# Sample data to insert
sample_data = [
    {"name": "Item 1", "value": 100},
    {"name": "Item 2", "value": 200},
    {"name": "Item 3", "value": 300},
    {"name": "Item 4", "value": 400}
]

async def insert_sample_data():
    # Optional: clear existing data
    await data_collection.delete_many({})

    # Insert sample data
    result = await data_collection.insert_many(sample_data)
    print(f"Inserted IDs: {result.inserted_ids}")

# Run the async function
if __name__ == "__main__":
    asyncio.run(insert_sample_data())
