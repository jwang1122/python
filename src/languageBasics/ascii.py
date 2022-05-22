"""
chr(i, /)
    Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.
"""
x = 0xF
print(x)
print(bin(x)) # bin() is built in function that convert int to binary format

x = u'世界您好'
# x1 = u'世界您好'
print(x) # hex() is built in function that convert int to hex format
print(x.encode('ascii','backslashreplace'))
# print(x1.encode('utf8'))

a = 0b01000001
print(a)

print(chr(a)) # chr() is built in function that convert int to ascii

b = 0b01000010
print(chr(b))

l = 0b01101100
print(chr(l))

u = 0b01110101
print(chr(u))

e = 0b01100101
print(chr(e))

