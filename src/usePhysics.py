from physics import *

t = Q(2, "s")
v = Q(3, 'm/s')
d = v * t
print(f"An object move with velocity of {v} for time {t} will travel {d}.")

s = Q(120, 'm')
v = s/t
print(f"if an object travels {s} within {t}, its velocity is {v}.")

a = v/t
print(f"An object's velocity is from 0 to {v} within {t}, it's acceleration is {a}.")

m = Q(80, 'kg')
f = m * a
print(f)

t = Q(.200, 's')
d = v * t
print(d)