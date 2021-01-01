n = 6
for num in range(1, n):
    print(' '*(n-num), end='')
    print((str(num)+' ') * num)

for num in range(n-2, 0, -1):
    print(' '*(n-num), end='')
    print((str(num)+' ') * num)