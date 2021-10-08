def upperSection(data):
    return sum(data)

def lowerSection(data):
    if yahtzee(data):
        return 50
    if largeStraight(data):
        return 40
    if smallStraight(data):
        return 30
    if kind(data)==4:
        return sum(data)
    if fullHouse(data):
        return 25
    return sum(data)

def kind(data):
    max = 0
    for i in range(len(data)):
        c = data.count(i)
        if c>max: max = c
    return max

def fullHouse(data):
    return kind(data) == 3 and len(set(data))==2

def smallStraight(data):
    s1,s2,s3 = {1,2,3,4}, {2,3,4,5}, {3,4,5,6}
    s = set(data)
    return s==s1 or s==s2 or s==s3

def largeStraight(data):
    return {1,2,3,4,5}==set(data)

def yahtzee(data):
    return len(set(data))==1

