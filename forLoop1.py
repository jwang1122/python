for i in range(10):
    print(i, end=' ')
print()


for i in (5,2,4,8,1):
    print(i)

for i in [3,7,9,11,23]:
    print(i)

for i in (5,2,4,8,1):
    for j in [3,7,9,11,23]:
        print(i + j)

for i in range(3):
    for j in range(5):
        for k in range(5):
            print(i,j,k)

for s in "Hello World!":
    print(s)

d1 = {"key1":"value1", "key2":"value2"}

for d in d1:
    print(d)