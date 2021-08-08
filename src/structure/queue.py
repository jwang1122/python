class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, obj):
        self.queue.append(obj)

    def dequeue(self):
        if len(self.queue)==0:
            print("The queue is empty.")
            return
        o = self.queue[0]
        self.queue.remove(o)
        return o
    
    def front(self):
        return self.queue[0]

    def rear(self):
        return self.queue[len(self.queue)-1]

if __name__ == '__main__':
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    q.enqueue("c")
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print()
    q.enqueue("a")
    q.enqueue("b")
    q.enqueue("c")
    print(q.front())
    print(q.rear())

