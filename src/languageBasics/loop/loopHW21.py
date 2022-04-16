"""
Use built-ins function: range(), len(), abs()
"""

x = [-1,  -4, -7]
y = [-3, 7, 6]

z = []
for i in range(len(x)):
    # print(x[i], y[i])
    z.append(abs(x[i]) + abs(y[i]))

print(z)