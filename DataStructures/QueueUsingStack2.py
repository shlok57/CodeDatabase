
'''
Queue using two stacks 
- Enqueue -> O(n)
- Dequeue -> O(1)
'''


class Queue:

    def __init__(self):

        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        while self.s1:
            self.s2.append(self.s1.pop())

        self.s1.append(x)

        while self.s2:
            self.s1.append(self.s2.pop())

    def dequeue(self):
        if not self.s1:
            return None
        return self.s1.pop()


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
q.enqueue(4)
q.enqueue(5)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
