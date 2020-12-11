class Sample(object):
    def __str__(self):
        return "SAMPLE"

class A(object):
    def __new__(cls):
        return Sample()

class B(object): # different way to write __new__()
    def __new__(cls):
        return super(B, cls).__new__(Sample)

if __name__ == '__main__':
    print(A())
    print(B())