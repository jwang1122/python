"""
@classmethod vs. @staticmethod
A class method takes cls as first parameter while a 
static method needs no specific parameters. 
"""
class C:
    classAttribute = 10
    @classmethod
    def f1(cls, *args):
        print(cls.classAttribute)
        for i in args:
            print(i, end=", ")
        print()

    @staticmethod
    def f2(**kwargs):
        print(C.classAttribute)
        print(kwargs)

if __name__ == '__main__':
    C.f1(1,2,3,4)
    C.f2(name="John", occupation="teacher")

    c1 = C()
    c1.classAttribute = 111 # it is not a good idea to allow instance modify class level attribute
    c1.f1(5,6,7,8)
    c1.f2(ssn="123456789")

    c2 = C()
    c2.f1(5,6,7,8)
    c2.f2(ssn="123456789")
