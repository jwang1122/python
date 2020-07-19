#create a tuple
t1 = (4, 6, 2, 8, 3, 1) 
print(t1)
t2 = (9,4,2)
t3 = t1 + t2 # add two tuple
print(t3)
#tuples are immutable, so you can not add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple
t1 = t1 + (9,)
print(t1)
#adding items in a specific index
t1 = t1[:5] + (15, 20, 25) + t1[:5]
print(t1)
#converting the tuple to list
listx = list(t1) 
#use different ways to add items in list
listx.append(30)
t1 = tuple(listx)
print(t1)
#insert tuple at give position [3]
t1 = t1[:3] + (9,8,7) + t1[3:]
print(t1)

d1 ={'k1': 'v1', 'k3': 'v3', 'k4': 'v4'}
print(d1)