from math import sqrt

def isInteger(value):
    return int(value)==value

for i in range(40, 30, -1):
    if i*i<1373:
        x = i
        break

x2 = x*x
y2=1373-x2

y = sqrt(y2)

print(f"{x*x} + {y*y} = 1373")

print(isInteger(2.3))
print(isInteger(2.0))
print(isInteger(2))
