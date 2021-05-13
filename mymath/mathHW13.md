* Write a Python program to calculate the discriminant value.


Note: The discriminant is the name given to the expression that appears under the square root (radical) sign in the quadratic formula.

$$ f(x) = ax^2 + bx +c $$
$$ discriminant = b^2 - 4ac $$
$$ x_1 = \frac {-b + \sqrt {discriminant} } {2a}$$
$$ x_2 = \frac {-b - \sqrt {discriminant} } {2a}$$
$$ x_{1,2} = \frac {-b \pm \sqrt {discriminant} } {2a}$$

if discriminant=0, there will be only one solution: $x = - \frac b {2a}$

if discriminat>0, there will be two real solutions.

if discriminat<0, there will be two complex solutions.


Expected output:

```
The a value: 4
The b value: 8
The c value: 2
Two Solutions (-0.293, -1.707). 
Discriminant value is: 32.0 > 0
4.0x*x + 8.0x + 2.0 = 0.0000

The a value: 4
The b value: 3
The c value: 2
No Real Solutions. Discriminant value is: -23.0 < 0
Two complex solutions (-0.375+0.599j, -0.375-0.599j)

The a value: 3
The b value: 6
The c value: 3
One Solution x=-1.000. 
Discriminant value is: 0.0
3.0x*x + 6.0x + 3.0 = 0.0000
```