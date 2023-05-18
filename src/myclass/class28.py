class OuterClass:
    class InnerClass:
        def __init__(self, inner_attr):
            self.inner_attr = inner_attr

    def __init__(self, outer_attr, inner_attr):
        self.outer_attr = outer_attr
        self.inner_obj = OuterClass.InnerClass(inner_attr)

    def print_attrs(self):
        print(f"Outer attribute: {self.outer_attr}")
        print(f"Inner attribute: {self.inner_obj.inner_attr}")

# Creating an instance of the outer class and accessing its attributes
outer_obj = OuterClass("outer value", "inner value")
outer_obj.print_attrs()
