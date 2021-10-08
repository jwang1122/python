"""
understand map and flatmap
"""
from functools import reduce

def map(iter, func):
    return [func(x) for x in iter] if iter else []

def getValue(obj):
    return reduce(lambda x,y: x, obj)  if obj else None

def flatmap(iter, func):
    v = getValue(iter)
    return [] if v is None else func(v)


if __name__ == '__main__':

    list1 = [2,3,4,5]
    # list1 = None
    x = map(list1, lambda x: x**2)
    print(x)

    x = flatmap(list1, lambda x: [x**2])
    print(x)

    x = flatmap([6], lambda x: [x**2])
    print(x)

    x = flatmap([], lambda x: [x**2])
    print(x)
    list_opt = [list1]
    print(list_opt)
    list5 = flatmap(list_opt, lambda x: [flatmap(y, lambda z: [z + 100]) for y in x])
    print(list5)