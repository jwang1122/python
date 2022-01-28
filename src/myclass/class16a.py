"""
class inheritence, review class level attribute
"""
class SuperClass:
    classAttribute = 10
    def __init__(self, a):
        self.instance = a
    
    def __repr__(self):
        return self.instance

    def superFunc(self):
        SuperClass.classAttribute *=3
        print(f'class attribute: {self.classAttribute}')

class SubClass(SuperClass):
    def __init__(self, a, b):
        SuperClass.__init__(self, a)
        self.b = b

    def __repr__(self):
        return self.instance + ", " + self.b

    def subFunc(self):
        print("This is subFunc() call...")

if __name__ == '__main__':
    obj1 = SuperClass("Super1")
    print(obj1)
    obj1.superFunc()

    obj2 = SuperClass("Super2")
    print(obj2)
    obj2.superFunc()

    obj3 = SubClass("Sub3", "Sub4")
    print(obj3)
    obj3.subFunc()
    obj3.superFunc()

    # obj4 = SubClass("Sub4")
    # print(obj4)
    # obj4.subFunc()
    # obj4.superFunc()

    print(isinstance(obj3, SubClass))
    print(isinstance(obj3, SuperClass))
    print(isinstance(obj1, SuperClass))
    print(isinstance(obj1, SubClass))