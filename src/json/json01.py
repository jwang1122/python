import json
from pprint import *

person = '{"name":"Bob", "languages":["Python", "Java"]}'
person_dict = json.loads(person)

pprint(person_dict)
print(person_dict['languages'])
