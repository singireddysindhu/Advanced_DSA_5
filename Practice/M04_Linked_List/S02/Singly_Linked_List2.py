'''
Singly linked list :
Algorithm:
1.Create a node
2. Insert data to the node
3.Connection btw the nodes
4.Traverse each node
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node1.next = node2
node2.next = node3
node3.next = node4
def traverse():
    curr=node1
    while curr :
        print(curr.data,end=" -> ")
        curr=curr.next
    print("None")
traverse()

'''
Operations:
1. Insertion
    a.Insertion at the beginning
    b.Insertion at the end
    c.Insertion after a particular node
2. Deletion
    a. Deletion at the beginning
    b. Deletion at the end
    c. Deletion after a particular node
3. Traverse
4.Updation
'''
'''
Operations on Singly Linked List

1. Insertion:
    a. At the beginning
    b. At the end
    c. At a given position
2. Deletion:
    a. At the beginning
    b. At the end
    c. At a given position
3. Traversal
4. Updation
'''
from platform import node


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    new_head = new_node
    del head
    return new_head

def delete_at_beginning(head):
    if head is None:
        print("Error: The linked list is empty.")
        return None
    head = head.next
    return head

def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        head = new_node
        return head
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

def delete_at_end(head):
    if head is None:
        print("Error: The linked list is empty.")
        return None
    if head.next is None:
        head = None
        return head
    current = head
    while current.next.next:
        current = current.next
    current.next = None
    return head

def insert_at_position(head, data, position):
    if head is None:
        print("Error: The linked list is empty.")
        return
    new_node = Node(data)
    new_node.next = node.next
    node.next = new_node 

def delete_at_position(head, position):
    if head is None:
        print("Error: The linked list is empty.")
        return None
    if position == 0:
        head = head.next
        return head
    current = head
    for i in range(position - 1):
        if current is None or current.next is None:
            print("Error: Position out of bounds.")
            return head
        current = current.next
    if current.next is None:
        print("Error: Position out of bounds.")
        return head
    current.next = current.next.next
    return head

def traverse(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
head = None

head = insert_at_beginning(head, 10)
head = insert_at_beginning(head, 20)
head = insert_at_beginning(head, 30)
print("Linked List after insertion at the beginning:")
traverse(head)

print("\nLinked List after insertion at the end:")
insert_at_end(head, 40)
traverse(head)
print()

print("Linked List after insertion at a given position:")
insert_at_position(head, 25, 2)
traverse(head)
print()

print("Linked List after deletion at the beginning:")
head = delete_at_beginning(head)
traverse(head)
print()

print("Linked List after deletion at the end:")
head = delete_at_end(head)
traverse(head)
print()

print("Linked List after deletion at a given position:")
head = delete_at_position(head, 1)
traverse(head)
print()