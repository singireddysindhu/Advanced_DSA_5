class Circular_Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * self.size
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if self.is_full():
            return "Queue is full"
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item 
        
    def dequeue(self):
        if self.front == -1:
            return "Queue is empty"
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size   

    def peek(self):
        if self.front == -1:
            return "Queue is empty"
        return self.queue[self.front] 
    
    def display(self):
        if self.front == -1:
            return "Queue is empty"
        elements = []
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()


    

 