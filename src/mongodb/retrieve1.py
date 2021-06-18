"""
Retrieve all books from mongoDB database
"""
from pymongo import MongoClient
from pprint import pprint
import json

client = MongoClient('localhost', 27017)
db = client['mydb']
bookdb = db.books

result = bookdb.find() # retrieve all
print(type(result))

for x in result:
    pprint(x)
