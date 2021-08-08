class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data

    def insert(self, obj):
        print(type(obj))
        obj.next = self.data.next
        self.data.next = obj

class Linkedlist:
    def __init__(self):
        self.head = None


if __name__ == '__main__':
    list1 = Linkedlist()
    mon = Node("Monday")
    tus = Node("Tuesday")
    wed = Node("Wednesday")
    thu = Node("Thursday")
    fri = Node("Friday")
    sat = Node("Saturday")
    sun = Node("Sunday")

    list1.head = mon
    mon.next = tus
    tus.next = wed
    wed.next = thu
    thu.next = fri
    fri.next = sat
    sat.next = sun

    obj = list1.head
    print(obj)
    for i in range(6):
        obj = obj.next
        print(obj)

    print()
    n = Node("No such day")
    wed.next = n
    n.next = thu
    obj = list1.head
    print(obj)
    for i in range(6):
        obj = obj.next
        print(obj)
