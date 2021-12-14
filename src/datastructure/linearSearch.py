"""
Worst case.

Big O, useful notation, Order of magnitude of complexity, upper bounds
O(1): constant time operation regardless times of trying.
O(n): linear search
O(log n): binary search. number of try=log_2(n) + 1, logarithm (n,tries), sort data first

"""
def linearSearch(list1, target):
    """
    Returns the index position of the target if found, else return None.
    """

    for i in range(0, len(list1)):
        if list1[i] == target:
            return i

def verify(index):
    if index: # if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in the list.")

if __name__ == '__main__':
    l1 = [3,1,5,34,2,39] # unsorted list
    verify(linearSearch(l1, 100))
    # print(x)
    print("Done.")