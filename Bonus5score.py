class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    def add(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.size += 1
    def pop(self):
        if self.top is not None:
            data = self.top.data
            self.top = self.top.next
            self.size -= 1
            return data
        return None
    def peek(self):
        return self.top.data
_case = 0
while True:
    n = input("Input : ")
    if n == '0':
        break
    try:
        if int(n):
            _case += 1
        print(f"case{_case}")
        now = Stack()
        cash = Stack()
        for i in range(int(n)):
            x = input("Input : ")
            if x == '0':
                break
            if x == 'B':
                if now.top is not None:
                    cash.add(now.pop())
                    print(f"Output : {now.peek()}")
            elif x == 'F':
                if cash.top is not None:
                    now.add(cash.pop())
                    print(f"Output : {now.peek()}")
            elif "." in x:
                now.add(x)
                print(f"Output : {now.peek()}")
    except:pass