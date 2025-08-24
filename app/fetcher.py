from pymongo import MongoClient
import os
from dotenv import load_dotenv
import pandas as pd

class Fetcher:
    """Retrieve documents from a MongoDB collection."""

    load_dotenv()

    def __init__(self):
        self.USER = os.getenv("USER")
        self.DB_NAME = os.getenv("DB_NAME")
        self.PASSWORD = os.getenv("PASSWORD")
        self.COLLECTION = os.getenv("COLLECTION")

        # Check if any critical environment variables are missing
        missing = [
            name for name, val in [
                ("USER", self.USER),
                ("PASSWORD", self.PASSWORD),
                ("DB_NAME", self.DB_NAME),
                ("COLLECTION", self.COLLECTION),
            ] if not val
        ]
        if missing:
            raise ValueError(f"Missing required environment variables: {', '.join(missing)}")

        # Build the MongoDB connection URI
        self.MONGO_URI = (
            f"mongodb+srv://{self.USER}:{self.PASSWORD}"
            f"@{self.DB_NAME}.gurutam.mongodb.net/"
        )

    def get_all_data(self):
        with MongoClient(self.MONGO_URI) as client:
            db = client[self.DB_NAME]
            collection = db[self.COLLECTION]
            # Return all documents while excluding the MongoDB-generated ``_id`` field
            res = list(collection.find({}, {"_id": 0}))
            return res




