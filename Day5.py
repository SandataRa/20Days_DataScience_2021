# Task N°5 
stack = []
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            raise Exception("Empty Stack")
        return self.stack.pop(len(self.stack)-1)
    
    def peek(self):
        if self.is_empty():
            raise Exception("Empty Stack")
        return self.stack[len(self.stack) -1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# INSTANCIATION
stack = Stack()
stack.push("Apple")
stack.push("Banana")
stack.push("Orange")
stack.push("Mango")
print(stack.size())
print(stack.pop())
print(stack.peek())
print(stack.size())

while stack.size() >0:
    print("The element %s has been removed" % stack.pop())

if stack.is_empty():
    print("Stack is empty!")

#Task N°6
class MyQueue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def peek(self):
        if self.is_empty():
            raise Exception("Empty queue")
        return self.items[0]

# INSTANCIATION
q = MyQueue()
q.enqueue("Marie")
q.enqueue("Joe")
q.enqueue("Karl")
q.enqueue("Lila")
print("Next person please: %s" % q.dequeue())
print("Peek the following person: %s" % q.peek())
print("Waiting list contains %d persons" % q.size())
print(q.items)

#Task N°6 Bis
from collections import deque

class MyQueue:

    def __init__(self, initial_values):
        self.items = deque(initial_values)

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def peek(self):
        if self.is_empty():
            raise Exception("Empty queue")
        return self.items[0]

# INSTANCIATION
q = MyQueue(['Marie','Joe','Karl','Lila'])
print("Next person please: %s" % q.dequeue())
q.enqueue('Marc')
print("Peek the following person: %s" % q.peek())
print("Waiting list contains %d persons" % q.size())
print(q.items)

