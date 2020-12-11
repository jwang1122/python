class Warehouse:
    purpose = 'storage' # class level attributes
    region = 'west'

w1=Warehouse()
print(w1.purpose, w1.region)

w2=Warehouse()
w2.region = 'east' # instance level attributes
print(w2.purpose, w2.region) # instance level attribute is used first