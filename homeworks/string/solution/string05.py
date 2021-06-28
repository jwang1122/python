s = "I am joining a python class."
words = s.split()
for i in range(len(words)):
    if words[i].endswith('.'):
        w = words[i]
        words[i] = w[:len(w)-1]
        
print(words)