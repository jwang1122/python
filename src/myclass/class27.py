class MyClass:
    class_attr = "Hello, I'm a class-level attribute"

    @classmethod
    def class_method(cls):
        print("Hello, I'm a class-level method!")
        print(cls.class_attr)

if __name__ == '__main__':
    # Accessing the class-level attribute
    print(MyClass.class_attr)

    # Calling the class-level method
    MyClass.class_method()

    obj1 = MyClass()
    obj1.class_attr = "Hello, I am obj1!" # python can create object attribute anywhere!!!

    obj2 = MyClass()
    print(obj2.class_attr)

    MyClass.class_attr = 'Hello, world!'
    print(f'obj1 class_attr: {obj1.class_attr}')
    print(f'obj2 class_attr: {obj2.class_attr}')
