class Student:
    def __init__(self, id, firstName, lastName, grade):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.grade = grade
    
    def __repr__(self):
        return self.firstName + " " + self.lastName

