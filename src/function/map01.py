# Example 1: using map with a lambda function
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)
# Output: [1, 4, 9, 16, 25]

# Example 2: using map with a named function
def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(double, numbers))
print(doubled_numbers)
# Output: [2, 4, 6, 8, 10]
