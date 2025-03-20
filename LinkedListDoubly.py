class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_to_left(self, data):
        new_node = Node(data)
        if self.head is None: 
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    def add_to_right(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    def display(self):
        current = self.head
        while current:
            print(current.data, end="")
            if current.next:
                print(" ", end="")
            current = current.next
        print()
    def delete_value(self, data):
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                print(f"Deleted {data}")
                return
            current = current.next
        print("Not Found.")
                
                

dll = DoublyLinkedList()
inputs = []
for _ in range(5):
    data = int(input())
    inputs.append(data)
dll.add_to_right(inputs[0]) 
dll.display()

dll.add_to_left(inputs[1])
dll.display()

dll.add_to_right(inputs[2])
dll.display()

dll.add_to_left(inputs[3]) 
dll.display()

dll.add_to_right(inputs[4])
dll.display()