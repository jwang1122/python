from collections import Counter
from pprint import pprint

def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :")
pprint(word_count("data/test1.txt"))