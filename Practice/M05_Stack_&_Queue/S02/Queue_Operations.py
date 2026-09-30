#Implementations of a Queue using linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue_LL:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
    def dequeue(self):
        if self.front is None:
            return "dequeue from empty queue"
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data 
    def peek(self):
        if self.front is None:
            return "front from empty queue"
        return self.front.data
    def display(self):
        if self.front is None:
            return "Queue is empty"
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next  
        print()  # for new line after displaying the queue
q=Queue_LL()
q.enqueue(10)
q.enqueue(100)
q.enqueue(1000)
q.enqueue(10000)
q.display()
q.dequeue()
q.display()
print(q.peek())
    