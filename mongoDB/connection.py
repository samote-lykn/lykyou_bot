from pymongo import MongoClient
from mongoDB.config import MONGO_DB_URI, MONGO_DB_DATABASE
from motor.motor_asyncio import AsyncIOMotorClient

# Create an AsyncIOMotorClient (async MongoDB client)
client = AsyncIOMotorClient(MONGO_DB_URI)

# Create a database
db = client[MONGO_DB_DATABASE]

# You can also expose the collections if you want to make them available directly
# collection = db['your_collection_name']

# This is to ensure that the connection is only made once
def get_db():
    return db