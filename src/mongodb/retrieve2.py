"""
Retrieve books from mongoDB under certain condition.
"""
from pymongo import MongoClient
from pprint import pprint
import json

client = MongoClient('localhost', 27017)
db = client['mydb']
bookdb = db.books

result = bookdb.find({'author': 'John Wang'}) # retrive books on given condition
for x in result:
    pprint(x)
