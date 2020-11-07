import requests
import json
from pprint import pprint

response = json.loads(requests.get("http://localhost:5000/books").text)
pprint(response)