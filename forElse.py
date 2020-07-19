for x in range(3):
    print(x)
else:
    print('Final x = %d' % (x))

for x in range(3):
    print(x)
print('Final x = %d' % (x))

for x in range(3):
    print(x)
    if x == 1:
        break
else:
    print('Final x = %d' % (x))

for x in range(3):
    print(x)
    if x == 1:
        break
print('Final x = %d' % (x))

"""
for:
    do stuff
    condition:
        break
else: # read as "else not break" or "else not condition"
    do more stuff
"""