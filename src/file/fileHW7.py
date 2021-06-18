filename = "data/test1.txt"
with open(filename) as f:
    text = f.read()

text = text.replace('\n', '')
print(text)