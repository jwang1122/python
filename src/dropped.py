h = float(input("Enter the height of the tower: "))
t = float(input("Enter the time interval: "))
s = 9.81*t**2/2
print("The height of the ball is",h-s,"meters")

t = float(input("Enter the time interval for the ball touch ground: "))
s = 9.81*t**2/2
print(f"The height of the tower is {s} meters")
