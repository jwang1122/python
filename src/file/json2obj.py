import json
from collections import namedtuple

def customStudentDecoder(studentDict):
    return namedtuple('Student', studentDict.keys())(*studentDict.values())

#Assume you received this JSON response
studentJsonData = '{"rollNumber": 1, "name": "Emma", "age":13, "grade":10}'

# Parse JSON into an object with attributes corresponding to dict keys.
student = json.loads(studentJsonData, object_hook=customStudentDecoder)

print(type(student))
print("After Converting JSON Data into Custom Python Object")
print(student.rollNumber, student.name, student.age)