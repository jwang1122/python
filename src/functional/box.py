"""
Understand wrapper box
"""
class Box:
    def __init__(self, value):
        self.value = value # value could be any type of data include function
    
    def getValue(self):
        return self.value


class Maybe(Box): # make Maybe an abstract class
    def __init__(self, value):
        raise NotImplementedError("Can't create objects of type Maybe: use Just(something) or Nothing.")

class Just(Maybe):
    def __init__(self, value): # 1st step: create container wrapper box
        super(Maybe, self).__init__(value)

    def __repr__(self):
        return "Just " + str(self.getValue())

    def fmap(self, function): # 2nd step: make this box a functor
        return Just(function(self.getValue()))

    def amap(self, function): # 3rd step: make this box a applicative
        pass

    def bind(self, function): # 4th step: make this box a monad
        pass

class Nothing(Maybe):
    def __init__(self):
        super(Maybe, self).__init__(None)

    def __repr__(self):
        return "Nothing"

    def fmap(self, function):
        return self

Nothing = Nothing()

def add3(num):
    return num + 3

if __name__ == '__main__':
    x = Just(10) # any object can be Just or Nothing
    print(x)
    y = x.fmap(add3)
    print(y)

    x=Nothing
    y = x.fmap(add3) # any object can be Just or Nothing, any function apply on Nothing return Nothing.
    print(y)

