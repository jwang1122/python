import json

with open('data/student.json') as f:
  students = json.load(f)

print(type(students))
print(students)
print(students["student3"]["lastname"])