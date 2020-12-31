import os

filename = 'data/test.txt'
info = os.stat(filename)
print(info.st_size)

with open(filename) as f:
    text = f.read()
print(len(text))