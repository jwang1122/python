for line in open('src/data/students.csv', 'r'):
    print(line.split(',')) # return each line as list
    print(line.strip().split(',')) # return each line as list

"""
cannot handle the situation if the data has , but not delimiter

for instance

item name,price,quantity
house,"120,599",10
iPhone,"1,999",30
"""

for line in open('src/data/item.csv', 'r'):
    print(line.strip().split(',')) # return each line as list
