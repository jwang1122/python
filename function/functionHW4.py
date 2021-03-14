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

def func1(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)

nums = [10, 20, 10, 40, 50, 60, 70]
target = 60
print(findTwoSum(nums, target))
print(func1(nums, target))
print(list(enumerate(nums)))