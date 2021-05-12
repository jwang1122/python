def discriminant():
    a = float(input('The a value: '))
    b = float(input('The b value: '))
    c = float(input('The c value: '))
    discriminant = (b**2) - (4*a*c)
    x1 = (-b + pow(discriminant, 0.5))/(2*a)
    x2 = (-b - pow(discriminant, 0.5))/(2*a)
    if discriminant > 0:
        print(f'Two Solutions ({x1:.3f}, {x2:.3f}). \nDiscriminant value is: {discriminant} > 0')
        print(f"{a}x*x + {b}x + {c} = {(a*x1*x1+b*x1+c):.4f}")
    elif discriminant == 0:
        print(f'One Solution x={x1:.3f}. \nDiscriminant value is: {discriminant}')
        print(f"{a}x*x + {b}x + {c} = {(a*x1*x1+b*x1+c):.4f}")
    elif discriminant < 0:
        print(f'No Real Solutions. Discriminant value is: {discriminant} < 0')


discriminant()
