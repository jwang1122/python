def swap(x, y):
    print(x, y)
    tmp = x
    x = y
    y = tmp
    print(x, y)

def swap1(l1, l2):
    for i in range(len(l1)):
        tmp = l1[i]
        l1[i] = l2[i]
        l2[i] = tmp

def changeContents(x):
    x['1'] = 'hello'

if __name__ == '__main__':
    s1 = "hello"
    s2 = "world"
    swap(s1, s2)
    print(s1, s2)

    l1 = [1,2,3]
    l2 = [4,5,6]
    print(f'before swap: {l1}, {l2}')
    swap1(l1, l2)
    print(f'after swap: {l1}, {l2}')

    d = {'1':'one', '2':'two'}
    changeContents(d)
    print(d)