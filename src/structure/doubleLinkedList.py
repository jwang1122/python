class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Adding data elements		
    def push(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode

    # Print the Doubly Linked list
    @staticmethod	
    def listprint(node):
        while (node is not None):
            print(node.data),
            last = node
            node = node.next

if __name__ == '__main__':
    dl = DoublyLinkedList()
    dl.push(12)
    dl.push(8)
    dl.push(62)
    DoublyLinkedList.listprint(dl.head)