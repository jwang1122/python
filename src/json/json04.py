
import json

person_dict = {"name": "Bob",
"languages": ["English", "Fench"],
"married": True,
"age": 32
}

with open('data/person.json', 'w') as json_file:
  json.dump(person_dict, json_file)