count = 0
for line in open("data/pokemon.csv"):
    count += 1
    print(f"{count:02d}: {line}", end='')
    if count >= 10:
        break    
