import math

print("17: I don't know how to do it")
"""
Google Search: Roman Numerals
"""
D=500
C=100
L=50
X=10
V=5
I=1
print("17: DCLXXVI in Roman Numeral is", D+C+L+X+X+V+I)

def roman_to_int(s):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    for i in range(len(s)):
        if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
            int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
        else:
            int_val += rom_val[s[i]]
    return int_val
s = "DCLXXVVI"
print(f"17: {s} in Roman Numeral is",roman_to_int(s))

print("11: 1983 rounded to the nearest ten is", round(1983/10)*10)
print("11: 1987 rounded to the nearest ten is", round(1987/10)*10)

s = "1296125"
print(f"03: The tens digit of {s} is", s[len(s)-2])