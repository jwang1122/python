def binarySearch(list1, target):
    first = 0
    last = len(list1) - 1

    while first <= last:
        midpoint = (first + last) //2
        if list1[midpoint] == target:
            return midpoint
        elif list1[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1


def verify(index):
    if index: # if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in the list.")

if __name__ == '__main__':
    l1 = [i for i in range(1, 10)]
    x = binarySearch(l1, 5)
    verify(x)