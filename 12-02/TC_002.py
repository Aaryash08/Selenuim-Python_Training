from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["company_DB"]
collections = db["c1"]
collections.insert_one({
    "name":"Shashank",
    "dep":"CSE",
    "course":"python",
    "salary":20000
})
result=collections.find_one({"name":"Shashank"})
print(result)