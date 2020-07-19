class Person(object): 
      
    # Constructor 
    def __init__(self, name): 
        self.name = name 
  
    # To get name 
    def getName(self): 
        return self.name 

    def isPerson(self):
        return True

    # To check if this person is employee 
    def isEmployee(self): 
        return False
  
  
# Inherited or Sub class (Note Person in bracket) 
class Employee(Person): 
  
    # Here we return true 
    def isEmployee(self): 
        return True

    def isManager(self):
        return False

class Manager(Employee):
    def isManager(self):
        return True

class Student(Person):
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def __repr__(self):
        return self.name + "(" + str(self.grade) + ")"


# Driver code 
person = Person("John Wang")  # An Object of Person 
print(person.getName(), "is employee:", person.isEmployee()) 
  
person = Employee("Devid Lee") # An Object of Employee 
print(person.getName(), "is person:", person.isPerson()) 
print(person.getName(), "is employee:", person.isEmployee()) 
print(person.getName(), "is manager:", person.isManager()) 

person = Manager("Eric Johnson") # An Object of Employee 
print(person.getName(), "is person:", person.isPerson()) 
print(person.getName(), "is employee:" ,person.isEmployee()) 
print(person.getName(), "is manager:", person.isManager()) 

person = Student("Samule Lee", 9)
print(person)
print(person.getName(), "is person:", person.isPerson()) 
