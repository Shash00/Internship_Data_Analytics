from pymongo import MongoClient
import pymongo as m

client = MongoClient("mongodb://localhost:27017/")

db = client["test"]

collection = db["faculty"]

query = {}
project = {"name":1, "salary":1, "_id":0}
for doc in collection.find(query).sort([("name", m.ASCENDING)]):
    print(doc["name"])
    