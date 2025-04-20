from pymongo import MongoClient


mongo=MongoClient("mongodb://localhost:27017/")

db=mongo["Mongo_CRUD"]
collection=db["Data"]

def insert(data:dict):
    collection.insert_one(data)
    return {"message": "Data inserted successfully"}

def get_one_by_name(name: str):
    doc = collection.find_one({"name": name})
    if doc and "_id" in doc:
        del doc["_id"]
    return doc
