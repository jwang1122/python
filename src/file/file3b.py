import json
# https://www.tutorialspoint.com/json/json_overview.htm

person = """{"menu": {
  "id": "file",
  "value": "File",
  "popup": {
    "menuitem": [
      {"value": "New", "onclick": "CreateNewDoc()"},
      {"value": "Open", "onclick": "OpenDoc()"},
      {"value": "Close", "onclick": "CloseDoc()"}
    ]
  }
}}"""
person_dict = json.loads(person)
print("16:", type(person_dict))
print("17:", person_dict)

# Output: ['English', 'French']
print("20:", person_dict['menu']['id'])
#print("21:", person_dict['menu']['popup']["menuitem"][1]["onclick"])
