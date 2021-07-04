import json

with open('src/data/student.json') as f:
  students = json.load(f)

print(type(students))
print(students)
print(students[1]["lastname"])