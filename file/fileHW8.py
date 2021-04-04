from collections import Counter
from pprint import pprint


def word_count(fname):
    with open(fname) as f:
        return Counter(f.read().split())


print("Number of words in the file :")
pprint(word_count("data/test1.txt"))

with open("data/test1.txt") as f:
    x = f.read().split()
    d = {}
    for w in x:
        if w in d.keys():
            d[w] = d[w] + 1
        else:
            d[w] = 1
pprint(d)