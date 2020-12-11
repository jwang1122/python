# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g

x = C()
y = x.f(3,-2)
print(y)
print(x.h())