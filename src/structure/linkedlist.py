"""
Implement Node class for linked list
"""
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data

    def insert(self, obj):
        obj.next = self.next
        self.next = obj

    @staticmethod
    def traverse(node):
        while node is not None:
            print(node.data)
            node = node.next

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
    Node.traverse(obj)

    print()
    n = Node("No such day")
    wed.insert(n)

    obj = list1.head
    Node.traverse(obj)