def removeValue(sampleList, val):
   return [value for value in sampleList if value != val]

list1 = [5, 20, 15, 20, 25, 50, 20]

resList = removeValue(list1, 20)
print(resList)