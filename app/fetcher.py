from pymongo import MongoClient
import os
from dotenv import load_dotenv
import pandas as pd

class Fetcher:

    load_dotenv()

    def __init__(self):
        self.HOST = os.getenv("HOST")
        self.DB_NAME = os.getenv("DB_NAME")
        self.PASSWORD = os.getenv("PASSWORD")
        self.COLLECTION = os.getenv("COLLECTION")
        # self.MONGO_URI = (f"mongodb+srv://{self.HOST}:{self.PASSWORD}@{self.DB_NAME}.gurutam.mongodb.nat/")
        self.MONGO_URI = (f"mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/")


    def get_all_data(self):
        with MongoClient(self.MONGO_URI) as client:
            db = client[self.DB_NAME]
            collection = db[self.COLLECTION]
            res =list(collection.find({},{"_id":0}))
            return res





f = Fetcher()
df =pd .DataFrame(f.get_all_data())
print(df.head(5).to_string())