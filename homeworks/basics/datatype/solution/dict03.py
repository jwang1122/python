s = 'I am so happy to learn Python which makes me happy, my parents happy, and also interested in Python Python Python Python Python.'
words = s.split()
d = {}
for w in words:
    if w.endswith(',') or w.endswith('.'):
        w = w[:len(w)-1]
    if w in d:
        d[w] = d[w]+1
    else:
        d[w] = 1
print(d)