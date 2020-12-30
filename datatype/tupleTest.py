"""
list contains sequence of data separated by comma, surrounded by brackets.方数组
tuple is sequence of data separated by comma, surrounded by parentheses。圆数组
l = [2,3,5,7,9]
t = (1,4,9,16,25)
dir(l)
dir(t)
"""
#create a tuple
tuplex = (4, 6, 2, 8, 3, 1) 
print(tuplex)

survey = (21,"China", True)
print("Age: %d, Country: %s, Knows_python: %s" %survey)
age, country, knows_python = survey # assign more values in one line.
print(f"Age = {age}")
print(f"Country = {country}")
print(f"Knows_python? {knows_python}")


#tuples are immutable, so you can not add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple
tuplex = tuplex + (9,) # without , (9) treated as an int
print(tuplex)
#adding items in a specific index
tuplex = tuplex[:5] + (15, 20, 25) + tuplex[:5]
print(tuplex)
#converting the tuple to list
listx = list(tuplex) 
#use different ways to add items in list
listx.append(30)
tuplex = tuple(listx)
print(tuplex)
#insert tuple at give position [3]
tuplex = tuplex[:3] + (9,8,7) + tuplex[3:]
print(tuplex)

a = (1,2,3)
b = (4,5,6)
c = tuple(zip(a, b))
print(c)

a, b, c = (1,2,3,4,5) # ValueError
a, b, c = (3, 5) # ValueError