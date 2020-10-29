from pymongo import MongoClient
from pprint import pprint
import json

client = MongoClient('localhost', 27017)
db = client['mydb']
bookdb = db.books

result = bookdb.find()
print(type(result))

for x in result:
    pprint(x)
