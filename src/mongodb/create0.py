from pymongo import MongoClient
import uuid

# CRUD: Create, Retrieve, Update, Delete

book = {
    "_id": uuid.uuid4().hex,
    "title": "Introduction of Java",
    "author": "John Wang",
    "read": False,
    "price": 12.69,
    "rating": 5
}

client = MongoClient('mongodb://localhost:27017')
db = client['mydb']
bookdb = db.books

result = bookdb.insert_one(book)
print(result.inserted_id)