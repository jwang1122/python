# Example 1: using filter with a lambda function
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
# Output: [2, 4]

# Example 2: using filter with a named function
def is_positive(x):
    return x > 0

numbers = [-2, -1, 0, 1, 2]
positive_numbers = list(filter(is_positive, numbers))
print(positive_numbers)
# Output: [1, 2]
