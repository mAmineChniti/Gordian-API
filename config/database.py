from pymongo import MongoClient
from os import environ
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

username = environ.get("USER")
password = environ.get("PASS")
database = environ.get("BASE")
collection = environ.get("COLLECTION")
host = environ.get("HOST")

client = AsyncIOMotorClient(f"mongodb+srv://{username}:{password}@{host}")
db = client[database]
users_collection = db[collection]