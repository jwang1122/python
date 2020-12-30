import inspect
import os

cf = inspect.currentframe()
# create empty dictionary
d = {}
print(type(d))
print(len(d))

d1 = {
    1: "Monday",
    2: "Tuesday",
    3: "Wendsday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}
print(f"{inspect.getframeinfo(cf).lineno}: {d1[4]}")
for key in d1.keys():
    print(f"{inspect.getframeinfo(cf).lineno}: {str(key)+'='+d1.get(key)}")
    
post = dict(message="SS Cotopaxi", language="English") # use dict() to create dict instance
print(f"{inspect.getframeinfo(cf).lineno}: {type(post)}")
print(f"{inspect.getframeinfo(cf).lineno}: {post}")
post["user_id"] = 221
print(f"{inspect.getframeinfo(cf).lineno}: {post}")
if 'location' in post:
    print(f'{inspect.getframeinfo(cf).lineno}: {post["location"]}')
else:
    print(f'{inspect.getframeinfo(cf).lineno}: "no location key"')
print(post.get("location", None)) # default value None

d = {"k1": "v1", "k2": "v2"}
print(f"{inspect.getframeinfo(cf).lineno}: {d}")
print(f'{inspect.getframeinfo(cf).lineno}: {d["k1"]}')

# modify dictionary => CRUD
d["k3"] = "v3"  # add new key-value pair
print(f"{inspect.getframeinfo(cf).lineno}: {d}")
print(f'{inspect.getframeinfo(cf).lineno}: {d.get("k4", "Not found")}') # find unexisting key-value
d["k1"] = "Hello"  # modify a key
print(f"{inspect.getframeinfo(cf).lineno}: {d}")
del d["k2"]  # delete a key
print(f"{inspect.getframeinfo(cf).lineno}: {d}")

d["weekday"] = d1  # dictionay in dictionary
print(f"{inspect.getframeinfo(cf).lineno}: {d}")
x = d.popitem()
print(f"{inspect.getframeinfo(cf).lineno}: {x}")
print(f"{inspect.getframeinfo(cf).lineno}: {d}")
x = d.pop("k3")
print(f"{inspect.getframeinfo(cf).lineno}: {x}")
print(f"{inspect.getframeinfo(cf).lineno}: {d}")


d.clear()  # clear dictionary
print(f"{inspect.getframeinfo(cf).lineno}: {d}")

# merge two dict
x = {"a": 1, "b": 2}
y = {"b": 3, "c": 4}
z = {**x, **y}
print(f"{inspect.getframeinfo(cf).lineno}: {z}") # no duplication, take y

z1 = {**y, **x}
print(f"{inspect.getframeinfo(cf).lineno}: {z1}") # no duplication, take x
