base = int(input("Enter the base number: "))
power = int(input("Enter the power number: "))

n = 1
for i in range(power):
    n *= base

print("Result:",n)