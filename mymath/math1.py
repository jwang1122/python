import math

x = math.sqrt(64)

print(x)

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

print(math.pi)
print(math.degrees(math.pi/2.0))
print(math.radians(90))
print(math.sin(math.pi/2.0))
print(math.cos(math.pi/4.0))
print(math.asin(1))
print(math.acos(0))
print("20:",math.comb(3,2)) #number of combinations of choosing 2 from 3 distinct elements without considering the order of elements.
print("21:",math.perm(3,2))
print(math.copysign(-4, 5))
p = (1,1)
q = (4,5)
print(math.dist(p,q))
p = (1,1,1)
q = (4,4,4)
print(math.dist(p,q))
print(math.erf(5))
print(math.exp(1))
print(math.expm1(1))
print(math.fabs(-2.341))
print(math.fmod(3.2,2.1))
x = [1.1,2.2,3.3]
print(math.fsum(x))
print(math.gcd(36,6))
print(math.isfinite(1234567890))
print(math.tan(math.pi/2))
print(math.isinf(math.tan(math.pi/2)))
print(math.isnan(3))
print(math.isqrt(12))
print(math.ldexp(5,2))
print(math.log(3, 10))
print(math.pow(10, 0.47712125471966244))
print(math.log10(3))
print(math.modf(5.25))
print(math.remainder(3,14))
print(math.sqrt(16))
