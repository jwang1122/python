def f(a, b):
    return a+b, a-b, a*b, a/b

a = int(input("Enter a value a: "))
b = int(input("Enter a value b: "))

print()
v1, v2, v3, v4 = f(a, b)
print(f"{a} + {b} = {v1}")
print(f"{a} - {b} = {v2}")
print(f"{a} \u00D7 {b} = {v3}")
print(f"{a} \u00F7 {b} = {v4}")