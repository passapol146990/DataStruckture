class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, value):
        self.stack.append(value)
        print(f"Pushed: {value}")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow: Cannot pop, stack is empty.")
            return None
        else:
            value = self.stack.pop()
            print(f"Popped: {value}")
            return value

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        else:
            return self.stack[-1]

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack elements are:", end=" ")
            for element in reversed(self.stack):
                print(element, end=" ")
            print()


s = Stack()

s.push(10)
s.push(20)
s.push(30)
s.display()

print("Top element is:", s.peek())

s.pop()
s.pop()
s.display()

s.pop()
s.pop()