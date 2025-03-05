# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None
#     def add(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node
#     def show(self):
#         current = self.head
#         while current:
#             print(current.data, end=" ")
#             current = current.next
#         print()
# sll = SinglyLinkedList()

# for _ in range(3):
#     data = int(input())
#     sll.add(data)

#     sll.show()

