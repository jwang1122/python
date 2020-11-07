"""
Using class level method
"""
import json

class Student(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"({self.first_name} {self.last_name})"

    @classmethod
    def from_string(cls, name_str):
        first_name, last_name = map(str, name_str.split(' '))
        student = cls(first_name, last_name)
        return student

    @classmethod
    def from_json(cls, json_string):
        jsonObj = json.loads(json_string)
        student = cls(jsonObj['first_name'], jsonObj['last_name'])
        return student

s1 = Student.from_string("John Wang")
print(s1)

s = """{"first_name":"Charles", "last_name":"Johnson"}"""
s2 = Student.from_json(s)
print(s2)