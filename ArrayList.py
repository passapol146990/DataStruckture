class NodeArrayList:
    def __init__(self, data):
        self.data = data
        self.next = None
class ArrayList:
    def __init__(self):
        self.head = None
        self.last = None
    def add(self, data):
        new_node = NodeArrayList(data)
        if self.head is None:
            self.head = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
    def pop(self):
        if self.head is None:
            return None
        if self.head.next is None:
            data = self.head.data
            self.head = None
            self.last = None
            return data
        node = self.head
        while node.next.next is not None:
            node = node.next
        data = node.next.data
        node.next = None
        self.last = node
        return data
    def peek(self):
        if self.head is None:
            return None
        return self.last.data
    def clear(self):
        self.head = None
        self.last = None
    def isEmpty(self):
        return self.head is None
