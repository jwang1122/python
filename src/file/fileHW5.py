from pprint import pprint

filename = "data/students.csv"
lines = []
with open(filename) as f:
    for line in f:
        lines.append(line.strip())

pprint(lines)