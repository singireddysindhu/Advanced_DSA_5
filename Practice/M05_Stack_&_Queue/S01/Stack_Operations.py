#stack operations:
#1. Push: Add an element to the top of the stack
#2. Pop: Remove the top element from the stack
#3. Peek/Top: View the top element without removing it
#4. IsEmpty: Check if the stack is empty
#5. Size: Get the number of elements in the stack 
class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        
        return "pop from empty stack"
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "peek from empty stack"

    
st = stack()
print(st.is_empty())  # True
st.push(1)
st.push(2)
print(st.peek())  # 2
print(st.size())  # 2
print(st.pop())  # 2
print(st.is_empty())  # False

# Stack implementation using linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack_LL:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def is_empty(self):
        return self.top is None

    def pop(self):
        if self.is_empty():
            return "pop from empty stack"
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data
    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count
    def peek(self):
        if self.is_empty():
            return "peek from empty stack"
        return self.top.data
st_ll = Stack_LL()
print(st_ll.is_empty())  # True
st_ll.push(1)
st_ll.push(2)
print(st_ll.peek())  # 2
print(st_ll.size())  # 2
print(st_ll.pop())  # 2
print(st_ll.is_empty())  # False


    