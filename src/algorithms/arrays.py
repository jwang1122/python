"""
Operations on Data Structure
1. Access and read values
2. Search for an arbitrary values
3. Insert values at any point into the structure
4. Delete the value in the Data Structure

"""
newList = [1,2,3]
result = newList[0]
# result = newList[8] # IndexError
print(result)

# linear search
if 1 in newList: print(True)

for n in newList:
    if n==1:
        print(True)
        break

