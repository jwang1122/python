from math import pi

def add(x, y):
    # support int + tuple 
    if type(y) in [tuple, list]:
        l = []
        for i in y:
            l.append(i+x)
        if type(y) ==list:
            return l
        return tuple(l)
    if type(x) in [tuple, list]:
        l = []
        for i in x:
            l.append(i+y)
        if type(x) ==list:
            return l
        return tuple(l)
    
    return x + y