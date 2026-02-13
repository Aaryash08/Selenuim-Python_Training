from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["company_DB"]
collection = db["c1"]

new_employee = {
    "name": "Kumar",
    "dep": "CSE",
    "course": "python",
    "salary": 20000
}
insert_result = collection.insert_one(new_employee)
print(f"Inserted Document ID: {insert_result.inserted_id}")


it_employees_cursor = collection.find({"dep": "CSE"})
print("\nDepartment Employees (Before Update):")
for emp in it_employees_cursor:
    print(emp)

query = {"name": "Kumar"}
new_values = {"$set": {"salary": 65000}}
update_result = collection.update_one(query, new_values)
print(f"\nModified count: {update_result.modified_count}")

print("\nDepartment Employees (After Update):")
updated_employees = collection.find({"dep": "CSE"})
for emp in updated_employees:
    print(emp)