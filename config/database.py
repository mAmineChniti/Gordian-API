from pymongo import MongoClient
from os import environ
from dotenv import load_dotenv
from pathlib import Path
from motor.motor_asyncio import AsyncIOMotorClient

dotenv_path = Path('/etc/secrets/.env')
load_dotenv(dotenv_path=dotenv_path)

username = environ.get("USER")
password = environ.get("PASS")
database = environ.get("BASE")
collection = environ.get("COLLECTION")
host = environ.get("HOST")

client = AsyncIOMotorClient(f"mongodb+srv://{username}:{password}@{host}")
db = client[database]
users_collection = db[collection]