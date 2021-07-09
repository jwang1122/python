"""
class inheritence, review class level attribute
"""
class SuperClass:
    classAttribute = 1
    def __init__(self, a):
        self.instance = a
    
    def __repr__(self):
        return self.instance

    def superFunc(self):
        SuperClass.classAttribute *=10
        print(self.classAttribute)

class SubClass(SuperClass):
    def subFunc(self):
        print(SuperClass.classAttribute)

obj1 = SuperClass("Super1")
print(obj1)
obj1.superFunc()

obj2 = SuperClass("Super2")
print(obj2)
obj2.superFunc()

obj3 = SubClass("Sub3")
print(obj3)
obj3.subFunc()
obj3.superFunc()

obj4 = SubClass("Sub4")
print(obj4)
obj4.subFunc()
obj4.superFunc()

print(isinstance(obj4, SubClass))
print(isinstance(obj4, SuperClass))
print(isinstance(obj1, SuperClass))
print(isinstance(obj1, SubClass))