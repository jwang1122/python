def addList(l1, l2):
    l = []
    for i in range(len(l1)):
        l.append(l1[i] + l2[i])
    return l

l1 = [1,2,3]
l2 = [4,5,6]
l = addList(l1, l2)
print(f"l = {l}")