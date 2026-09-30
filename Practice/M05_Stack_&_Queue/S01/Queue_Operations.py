#Queue Operations:
#1. Enqueue: Add an element to the rear of the queue
#2. Dequeue: Remove an element from the front of the queue
#3. Front: View the first element without removing it
#4. Rear: View the last element without removing it
#5. IsEmpty: Check if the queue is empty
#6. IsFull: Check if the queue is full (for fixed-size queues)

#Implementation of Queue using python List
class Queue:
    def __init__(self):
        self.items = []
# enqueue time complexity is O(1) 
    def enqueue(self, item):
        self.items.append(item)

    def is_empty(self):
            return len(self.items) == 0
#dequeue time complexity is O(n) 
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "dequeue from empty queue"

    def front(self):
        if not self.is_empty():
            return self.items[0]
        return "front from empty queue"

    def display(self):
        if self.is_empty():
            return "Queue is empty"
        for item in self.items:
            print(item, end=" ")

queue = Queue()
print(queue.is_empty())  # True 
queue.enqueue(1)
queue.enqueue(2)    
queue.display()  # 1 2 
queue.dequeue()  # 1
queue.display()  # 2
queue.front()  # 2

