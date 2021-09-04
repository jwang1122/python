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
        return function(self)

    def amap(self, functionValue): # 3rd step: make this box a applicative
        pass

    def bind(self, function): # 4th step: make this box a monad
        return function(self)

    def __mul__(self, function):
        return self.fmap(function)

    def __rshift__(self, function): # 5th step: override >> operator
        # if not isinstance(function, Maybe):
        #     error_message = 'The function must return Maybe.'
        #     raise TypeError(error_message)

        # if not callable(function):
        #     function = lambda _ : function

        return self.bind(function)

class Nothing_(Maybe):
    def __init__(self):
        super(Maybe, self).__init__(None)

    def __repr__(self):
        return "Nothing"

    def fmap(self, function):
        return self

    def amap(self, functionValue):
        return self

Nothing = Nothing_()

def curry(func):
    numArgs = len(inspect.signature(func).parameters)

    def buildReader(argumentValues, numArgs):
        if numArgs == 0:
            return func(*argumentValues)
        else:
            return lambda x: buildReader(argumentValues + [x], numArgs)
    return Reader(buildReader([], numArgs))
    
def add3(num):
    return Just(num.getValue() + 3)

@curry
def divid(a, b):
    if a is Nothing or b is Nothing or b==0:
        return Nothing
    return Just(a.getValue()/b.getValue())

if __name__ == '__main__':
    x = Just(10) # any object can be Just or Nothing
    print(x)
    y = x.fmap(add3)
    print(f"83: {y}")
    y = x * add3
    print(f"85: {y}")

    x=Nothing_()
    y = x.fmap(add3) # any object can be Just or Nothing, any function apply on Nothing return Nothing.
    print(y)

    x = divid(Just(4), Just(5)) # box good value
    print(x)

    x = divid(Just(4), Nothing) # box bad value
    print(x)

    x = divid(Just(4), 0)
    print(x)

    x = Just(2).bind(add3)
    print(x)

    x = Just(5)>>add3
    print(x.getValue()) # open box