class List():
    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value

    def bind(self, f): # bind function make List to be monad
        result = list(map(f, self.value))
        return List(result)
        
    def __str__(self):
        return 'List(' + ', '.join(map(str, self.value)) + ')'
        
    def __mul__(self, f): # override * operator
        return self.bind(f)

if __name__ == '__main__':
    x = List([1,2,3])
    f = lambda s: s.zfill(4)
    n = x * str * f
    print(n)