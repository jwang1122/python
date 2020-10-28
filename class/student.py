class Student(object):
    def __init__(self):
        

    @classmethod
    def from_string(cls, name_str):
        first_name, last_name = map(str, name_str.split(' '))
        student = cls(first_name, last_name)
        return student

    @classmethod
    def from_json(cls, json_obj):
        # parse json...
        return student

