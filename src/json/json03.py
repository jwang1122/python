"""
dict to json string
"""
import json

person_dict = {'name': 'Bob',
'age': 12,
'children': 2
}
person_json = json.dumps(person_dict)

# Output: {"name": "Bob", "age": 12, "children": null}
print(person_json)