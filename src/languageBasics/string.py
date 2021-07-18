"""
str: python use '', or "" for string variable assignment
"""

s = "Meet me at Python class."
print("Double quota", type(s))
s = 'Meet me at Python class.'
print("Single quote",type(s))
s = """Meet me at Python class.""" # triple double quotation
print(type(s))
s = '''Meet me at Python class.''' # triple single quotation
print(type(s))
s = "John said: 'I like Python.'"
print(s)
s = 'John said: "I like Python."'
print(s)
s = '''john said: "I'm Python developer."''' # use escape squence, \'
print("18: "+s)

s = 'meet me at python class.' # single or double quote are equivalent
print(type(s))
print(s)

# string is iterable
for item in s:
    print(item, end=' ')
print()

# string slicing
print(s[4:10])
print(s[1:100])
print(s[1:100:2]) # s[[start]:[stop]:[step]]
print(s[::])
print(s[-1]) # get last letter
print(s[::-1]) # revers the string
print(s[-2:-8:-1]) # reverse the part of the string 

# string functions (title, capitalize, endswith, isalnum, isdigit, strip)
print(s.title())
print(s.capitalize())

s="happy,"
if s.endswith(','):
    s = s[:-1] # git rid of last
    print(26,s)  

s = "   happy   "
s = s.strip()
print(f"[{s}]")

s = ',,,happy.,,,'
s = s.strip(',.')
print(f"34: [{s}]")

s = '101F'
s = s.strip('F')
print(f"38: [{s}°F]")

s = "123"
print(s.isalnum())
print(s.isalpha())
print(s.isdigit())

s='92F'
print(s.endswith('F'))
print(s[:-1])
x = int(s[:-1])
print(x+29)

s="print.md"
index = s.index('.')
print(s[index:])

# operators on string: +, *
s1 = "John"
s2 = "Wang"
fullName = s1 + ' ' + s2

n="2"
s = n*5
print(type(s))
print(n*5)

