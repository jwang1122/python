import inspect
import os

"""
String processing
"""
f = inspect.currentframe()
s = "this is\ta Test."
print(f"{inspect.getframeinfo(f).lineno}: {s.capitalize()}")
print(f"{inspect.getframeinfo(f).lineno}: {s.title()}")
print(f"{inspect.getframeinfo(f).lineno}: {s.upper()}")
print(f"{inspect.getframeinfo(f).lineno}: {s.lower()}")
print(f"{inspect.getframeinfo(f).lineno}: {s.count('t')}")
print(f"{inspect.getframeinfo(f).lineno}: {s.center(80)}")
s2 = "THIS IS\tA TEST."
print(f"{inspect.getframeinfo(f).lineno}: {s==s2}") # they are different by case
print(f"{inspect.getframeinfo(f).lineno}: {s.casefold()==s2.casefold()}") # ignore case
print(f"{inspect.getframeinfo(f).lineno}: {s.expandtabs(tabsize=8)}") # replace tab character with space

print(f"{inspect.getframeinfo(f).lineno}: {s.endswith('.')}")
print(f"{inspect.getframeinfo(f).lineno}: {s.startswith('this')}")
print(f"{inspect.getframeinfo(f).lineno}: {s.find('is')}")
print(f"{inspect.getframeinfo(f).lineno}: {s.index('is')}")
print(f"{inspect.getframeinfo(f).lineno}: {s.find('is', 3)}")
print(f"{inspect.getframeinfo(f).lineno}: {s.find('john')}")

print(f"{inspect.getframeinfo(f).lineno}: {'123'.zfill(5)}")

a, b = 11, 31
c = a + b
s = "{0} + {1} = {2}"
print(f"{inspect.getframeinfo(f).lineno}: {s.format(a, b, c)}")

s = "2a"
print(f"{inspect.getframeinfo(f).lineno}: {s.isalnum()}")
print(f"{inspect.getframeinfo(f).lineno}: {s.isalpha()}")
s = "12"
print(f"{inspect.getframeinfo(f).lineno}: {s.isnumeric()}")
print(f"{inspect.getframeinfo(f).lineno}: {s.isdigit()}")

print(f"{inspect.getframeinfo(f).lineno}: {'3.4'.isdecimal()}")
print(f"{inspect.getframeinfo(f).lineno}: {'1.2'.isdigit()}")

# check if a string is a float number
f1 = "2.34"
print(f"{inspect.getframeinfo(f).lineno}: {f1 + str(3.5)}") # string concatination
f1 = float(f1) if f1.replace('.', '', 1).isdigit() else f1
print(f"{inspect.getframeinfo(f).lineno}: {f1 + 3.5}")
print(f"{inspect.getframeinfo(f).lineno}: {type(f1)}")

print(f'{inspect.getframeinfo(f).lineno}: {"::".join("abc")}')
print(f'{inspect.getframeinfo(f).lineno}: {" of ".join(("A", "Heart"))}')
print(f'{inspect.getframeinfo(f).lineno}: {" of ".join(["1", "10", "100"])}')

# build csv(comma separated value) file use join() function
person = {"name":"John", "ssn":"999-99-9999", "gender":"M"}
print(f'{inspect.getframeinfo(f).lineno}: {",".join(person)}')
print(f'{inspect.getframeinfo(f).lineno}: {",".join(person.values())}')

print(f'{inspect.getframeinfo(f).lineno}: {"   123".lstrip(" " )}')
print(f'{inspect.getframeinfo(f).lineno}: {"   123   ".strip()}')
print(f'{inspect.getframeinfo(f).lineno}: {"1,2,3,4,5".split(",")}')
print(f'{inspect.getframeinfo(f).lineno}: {"1,2,3,4,5".split(",", 2)}')
print(f'{inspect.getframeinfo(f).lineno}: {"1,2,3,4,5".rsplit(",", 2)}')
s = "1,2\n3\n4,5".splitlines()
print(f'{inspect.getframeinfo(f).lineno}: {s}')

print(f'{inspect.getframeinfo(f).lineno}: {"1,234".partition(",")}')

print(f'{inspect.getframeinfo(f).lineno}: {"1234567".replace("345", "abc", 3)}')
print(f'{inspect.getframeinfo(f).lineno}: {"1234567".rfind("89")}') # return -1 since not found
print(f'{inspect.getframeinfo(f).lineno}: {"1234567123456".index("34")}') # index from left
print(f'{inspect.getframeinfo(f).lineno}: {"1234567123456".rindex("34")}') # index from right

import pandas as pd

Data = {'Product': ['ABC', 'XYZ'], 'Price': ['250.88', '270.43']}

df = pd.DataFrame(Data)
df['Price'] = df['Price'].astype(float)

print(f"{inspect.getframeinfo(f).lineno}: ")
print(df)
print(f"{inspect.getframeinfo(f).lineno}: ")
print(df.dtypes)
