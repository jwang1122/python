from math import pi

height = float(input('Height of cylinder: '))
radian = float(input('Radius of cylinder: '))
print()
volume = pi * radian * radian * height
sur_area = ((2*pi*radian) * height) + ((pi*radian**2)*2)
print(f"Volume is: {volume:.3f}")
print(f"Surface Area is: {sur_area:.3f}")