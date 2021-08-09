temps = [("Berlin", 29),("Cairo", 36),("Buenos Aires", 19),("Los Angeles", 26), \
        ("Tokyo", 27), ("New York", 28),("London", 22),("Beijing", 32)]

byCity = lambda data: data[0] # byCity is callable

print("Sorted by city:")
x = sorted(temps,key=byCity)
print(x)

print("Sorted by temperature:")
x = sorted(temps, key=lambda data:data[1])
print(x)

x = sorted(temps) #sorted by first item
print(x)

print(temps) # original list has no change
