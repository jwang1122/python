# https://python.plainenglish.io/unit-conversion-in-python-3ee480d4b19c

import sympy.physics.units as u
from sympy.physics.units.systems import SI

distance = u.Quantity('d')
SI.set_quantity_dimension(distance, u.length)
SI.set_quantity_scale_factor(distance, 5.*u.meter)

z = u.convert_to(distance, u.yards)
print(z)

eV = u.Quantity('eV')
SI.set_quantity_dimension(eV, u.energy)
SI.set_quantity_scale_factor(eV, 1 * u.electronvolt)
z = u.convert_to(eV, u.joule)
print(z)

# define a force formula
# newton = sympy.Eq(F, G * m * M / r**2)
# G_ = sympy.solve(newton, G).pop()
# print(G_)