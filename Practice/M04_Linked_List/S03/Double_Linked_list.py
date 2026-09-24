
'''
Double Linked List :
the data can be stored in nodes
Node --> 3 parts
1. data
2.Previous 
3.Next

Algorith:
1. Create a node
2. Insert a node 
3. Connection
4. Traversal


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
# Connection
node1.next = node2
node2.prev = node1

node2.next = node3
node3.prev = node2  

node3.next = node4
node4.prev = node3

def traverse():
    current = node1
    while current:
        print(current.data,end=" <-> ")
        current = current.next
print("None")
traverse()
#write the code to print in reverse order
def traverse_reverse():
    current = node4
    while current:
        print(current.data,end=" <-> ")
        current = current.prev
    print("None")
traverse_reverse()
'''

#insert a node at the beginning
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    if head is not None:
        head.prev = new_node
    return new_node

#insert a node at the end
def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    new_node.prev = current
    return head

#insert a node at a given position
def insert_at_position(head, data, position):
    new_node = Node(data)
    if position == 0:
        return insert_at_beginning(head, data)
    current = head
    for i in range(position - 1):
        if current is None:
            print("Error: Position out of bounds.")
            return head
        current = current.next
    if current is None:
        print("Error: Position out of bounds.")
        return head
    new_node.next = current.next
    new_node.prev = current
    if current.next is not None:
        current.next.prev = new_node
    current.next = new_node
    return head

def traverse(head):
    current = head
    while current:
        print(current.data, end=" <-> ")
        current = current.next
    print("None")
head = None
head = insert_at_beginning(head, 10)
head = insert_at_beginning(head, 20)
head = insert_at_beginning(head, 30)
print("Linked List after insertion at the beginning:")
traverse(head)
print()
head = insert_at_end(head, 40)
head = insert_at_end(head, 50)
print("Linked List after insertion at the end:")
traverse(head)
print()
head = insert_at_position(head, 25, 2)
print("Linked List after insertion at a given position:")
traverse(head)
print()