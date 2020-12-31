"""
Find a pair of elements (indices of the two numbers) 
from a given array whose sum equals a specific target number. 
"""
def findTwoSum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return (lookup[target - num], i)
        lookup[num] = i


nums = [10, 20, 10, 40, 50, 60, 70]
target = 60
print(findTwoSum(nums, target))