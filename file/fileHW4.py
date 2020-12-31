with open('./data/students.csv', 'a') as f:
    f.write('9711,Charles,Martine,93\n')

with open('./data/students.csv') as f:
    text = f.read()

print(text)

print("Done.")