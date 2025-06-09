from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Select the database and collection
db = client["taller_mongo"]
collection = db["clientes"]

# Find one document
result = collection.find_one()
print(result)