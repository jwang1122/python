class MyClass:
    def __init__(self):
        self.status1 = True
        self.status2 = True

    def first(self):
        print("first function...")
        self.second() # pre-defined lifecycle

    def second(self):
        print("second function...")
        self.third()

    def third(self):
        print("third function...")
        
class MyClass1(MyClass):
    def second(self):
        if self.status1:
            pass

if __name__ == '__main__':
    obj1 = MyClass()
    obj1.first()
    obj1 = MyClass1()
    obj1.first()
    print(obj1.status1)

