from pymongo import MongoClient
import os
from dotenv import load_dotenv
import pandas as pd

class Fetcher:

    load_dotenv()

    def __init__(self):
        self.USER = os.getenv("USER")
        self.DB_NAME = os.getenv("DB_NAME")
        self.PASSWORD = os.getenv("PASSWORD")
        self.COLLECTION = os.getenv("COLLECTION")
        self.MONGO_URI = f"mongodb+srv://{self.USER}:{self.PASSWORD}@{self.DB_NAME}.gurutam.mongodb.net/"


    def get_all_data(self):
        with MongoClient(self.MONGO_URI) as client:
            db = client[self.DB_NAME]
            collection = db[self.COLLECTION]
            res =list(collection.find({},{"_id":0}))
            return res




