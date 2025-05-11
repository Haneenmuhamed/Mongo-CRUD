from pymongo import MongoClient


mongo=MongoClient("mongodb://localhost:27017/")

db=mongo["Mongo_CRUD"]
collection=db["Data"]


collection.create_index([
    ("name", "text"),
    ("job", "text"),
    ("address", "text")
])