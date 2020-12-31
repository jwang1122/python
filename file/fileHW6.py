from pprint import pprint

filename = "data/pokemon.csv"
n = 10
lines = []

with open(filename) as pokemon:
    for line in pokemon:
        lines.append(line.strip())

start = len(lines) - n
output = lines[start:]
for line in output:
    print(line)