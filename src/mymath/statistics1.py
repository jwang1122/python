"""
statistics.mean(data) 

Return arithmetic mean (“average”) of data.
"""
from statistics import mean, fmean, geometric_mean

l = [1, 2, 3, 4, 5, 6, 7]
m = mean(l)

print(m)

from fractions import Fraction as Frac

x = Frac(1,2)
print(x)
m = mean([Frac(3, 7), Frac(1, 21), Frac(5, 3), Frac(1, 3)])
print(f"Fraction mean: {m}")
print(float(m))

from decimal import Decimal as D
m = mean([D("0.5"), D("0.75"), D("0.625"), D("0.375")])
print(f"mean: {m}")

m = fmean([3.5, 4.0, 5.25])
print(f"float mean: {m}")

