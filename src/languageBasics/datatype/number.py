a = 5  # int
print(type(a))

a = 1.01235 # float
print(type(a))

a = 2 - 4j # complex
print(type(a))
print(a)
# a = int(a) # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
# print(type(a))

a = '123'
print(type(a))

a = int(a)
print(type(a))

a = float(a)
print(type(a))
print(a)

a = complex(a)
print(type(a))
print(a)
