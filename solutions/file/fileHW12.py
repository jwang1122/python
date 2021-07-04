def file_lengthy(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


print("Number of lines in the file: ", file_lengthy("data/pokemon.csv"))

fname = "data/pokemon.csv"
with open(fname) as f:
    count=0
    for line in f:
        count += 1
    print(f"Number of lines in file {fname}: {count}")


l = ["January",'Febuary','March','April','May','June','July','August','September','October','Novenber',"December"]
for i, x in enumerate(l):
    print(f"{i+1}: {x}")