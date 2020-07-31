# create empty dictionary
d = {}
print(type(d))
print(len(d))

d1 = {1:"Monday",2:"Tuesday",3:"Wendsday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
print(d1[4])

d = {"k1":"v1","k2":"v2"}
print(d)
print(d["k1"])

# modify dictionary => CRUD
d["k3"] = "v3" # add new key-value pair
print(d)
print(d.get("k4","Not found")) # find unexisting key-value
d["k1"] = "Hello" # modify a key
print(d)
del d["k2"] # delete a key
print(d)

d["weekday"] = d1 # dictionay in dictionary
print(d)


d.clear() # clear dictionary
print(d)

# merge two dict
x = {'a':1, 'b':2}
y = {'b':3, 'c':4}
z = {**x, **y}
print(z)
z1 = {**y, **x}
print(z1)