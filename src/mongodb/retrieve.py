"""
Retrieve one book from mongoDB database.
"""
from pymongo import MongoClient
from pprint import pprint
import json

client = MongoClient('localhost', 27017)
db = client['mydb']
bookdb = db.books

_id = '3f3dbfaf1c3f4fd5a2ae43e989144e4d'
result = bookdb.find_one({'_id': _id}) # retrieve one book with given _id
pprint(result)
# file1 = open("book.json","a")
# json.dump(result, file1)
# file1.close()
# print("the book info is saved to book.json file.")