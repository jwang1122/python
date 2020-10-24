# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = student_from_dict(json.loads(json_string))

from typing import Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class StudentElement:
    firstname: str
    lastname: str
    id: int

    def __init__(self, firstname: str, lastname: str, id: int) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.id = id

    @staticmethod
    def from_dict(obj: Any) -> 'StudentElement':
        assert isinstance(obj, dict)
        firstname = from_str(obj.get("firstname"))
        lastname = from_str(obj.get("lastname"))
        id = int(from_str(obj.get("id")))
        return StudentElement(firstname, lastname, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["firstname"] = from_str(self.firstname)
        result["lastname"] = from_str(self.lastname)
        result["id"] = from_str(str(self.id))
        return result


class Student:
    students: List[StudentElement]

    def __init__(self, students: List[StudentElement]) -> None:
        self.students = students

    @staticmethod
    def from_dict(obj: Any) -> 'Student':
        assert isinstance(obj, dict)
        students = from_list(StudentElement.from_dict, obj.get("students"))
        return Student(students)

    def to_dict(self) -> dict:
        result: dict = {}
        result["students"] = from_list(lambda x: to_class(StudentElement, x), self.students)
        return result


def student_from_dict(s: Any) -> Student:
    return Student.from_dict(s)


def student_to_dict(x: Student) -> Any:
    return to_class(Student, x)
