class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class double_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def delete_node_at_beginning(self):
        if self.head is None:
            return
        self.head = self.head.next
        del_node = self.head
        del del_node

    def delete_node_at_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.prev.next=None
        temp.next
        del_node=temp
        del del_node

    def delete_node_at_position(self, position):
        if self.head is None:
            return
        if position == 0:
            self.delete_node_at_beginning()
            return
        temp = self.head
        for i in range(position):
            if temp is None:
                return
            temp = temp.next
        if temp is None:
            return
        if temp.next is not None:
            temp.next.prev = temp.prev
        if temp.prev is not None:
            temp.prev.next = temp.next
        del_node = temp
        del del_node

    def traverse(self):
        if self.head is None:
            return 
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def count_nodes(self):
        if self.head is None:
            return 0 
        if self.head.next is None:
            return 1
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count
    
dll=double_linked_list()
dll1=double_linked_list()
dll.insert_at_beginning(10)
dll.insert_at_beginning(20)
dll.insert_at_beginning(30)
dll.traverse()
dll1.insert_at_end(10)
dll1.insert_at_end(20)
dll1.insert_at_end(30)
dll1.traverse() 
dll2=double_linked_list()
dll2.insert_at_beginning(10)
dll2.insert_at_end(20)
dll2.insert_at_beginning(30)
dll2.traverse()
print(dll2.count_nodes())
dll2.delete_node_at_beginning()
dll2.traverse()
dll1.delete_node_at_end()
dll1.traverse()
dll2.delete_node_at_position(1)
dll2.traverse()