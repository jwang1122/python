"""
load json from a file
"""
import json

with open('data/books.json') as book:
    data = json.load(book)

print(data)