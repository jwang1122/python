class Length:
    def __init__(self, name):
        self


unitTypes = {'Length':['km','m','mm','mile','feet','inch'],'Mass':['kg','g'], 'Time':['s','m','h']}

class PhysicalUnit(dict):
    def __init__(self, name, type):
        self.name = name
        self.type = type
        
    def convert(self, to):
        pass
        
    def addUnit(self, unit):
        pass

class Quantity:
    def __init__(self, value, unit):
        self.value = value
        self.symble = unit

    def __repr__(self):
        return ' '.join([str(self.value), self.unit]) 

    def convert(self, targetUnit):
        pass

class Q(Quantity):
    pass

if __name__ == '__main__':
    d = Q(2, 'km')
    print(d)

    d.convert('m')


