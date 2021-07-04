def multiplyList(l):
    result = 1
    for i in l:
        result *= i
    return result

l = [8, 2, 3, -1, 7]
m = multiplyList(l)
print(m)