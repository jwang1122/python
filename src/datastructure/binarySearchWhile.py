"""
use while loop for binary search
"""
def binarySearch(arr, first_index, last_index, target):
    mid = int((first_index + last_index)/2)
    while first_index<=last_index:
        if arr[mid] < target:
            first_index = mid + 1
        elif arr[mid] == target:
            return mid
        else:
            last_index -= mid
        mid = int((first_index+last_index)/2)
    if first_index > last_index:
        return -1

if __name__ == '__main__':
    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120 ]
    target=41
    last_index = len(arr)-1
    result = binarySearch(arr, 0, last_index, target)
    if result==-1:
        print(f"'{target}' is not found.")
    else:
        print(f"'{target}' is found at index {result}.")
    print("Done.")

    