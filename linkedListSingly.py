class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def show(self):
        current = self.head
        while current:
            print(current.data, end="")
            if current.next:
                print(" ", end="")
            current = current.next
        print()
sll = SinglyLinkedList()
a = []
for _ in range(3):
    data = int(input())
    a.append(data)
for i in a:
    sll.add(int(i))
    sll.show()
