class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.mathourses = set()

    def addCourse(self, mathourse):
        self.mathourses.add(mathourse)

    def getCourses(self):
        return self.mathourses

class Course:
    def __init__(self, name):
        self.name = name
        self.students = []
    
    def __repr__(self):
        return self.name

    def addStudent(self, student):
        self.students.append(student)
        student.addCourse(self)

    def getNumberOfStudents(self):
        return len(self.students)

if __name__ == '__main__':
    s1 = Student("John", 14, 88)
    s2 = Student("David", 14, 98)
    s3 = Student("Bob", 14, 68)
    math = Course('Math-123')
    math.addStudent(s1)
    math.addStudent(s2)
    math.addStudent(s3)
    print(math.getNumberOfStudents())
    physimaths = Course("Phys-456")
    s1.addCourse(physimaths)
    s1.addCourse(physimaths)
    s1.addCourse(physimaths)
    print(s1.getCourses())
    


    