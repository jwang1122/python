from sympy.abc import *
import sympy
from sympy.physics.units.systems.si import dimsys_SI

newton = sympy.Eq(F, G * m * M / r**2)

G_ = sympy.solve(newton, G).pop()

print(G_)



