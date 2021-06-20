def recursiveBinarySearch(list1, target):
    if len(list1) == 0:
        return False
    else:
        midpoint = (len(list1))//2

        if list1[midpoint] == target:
            return True
        else:
            if list1[midpoint] < target:
                return recursiveBinarySearch(list1[midpoint+1:], target)
            else:
                return recursiveBinarySearch(list1[:midpoint], target)

def verify(result):
    print("Target found: ", result)

numbers = [i for i in range(1, 9)]
print(numbers)
x = recursiveBinarySearch(numbers, 4)
verify(x)
x = recursiveBinarySearch(numbers, 12)
verify(x)