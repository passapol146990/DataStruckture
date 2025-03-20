class QueueArray:
    def __init__(self, max_size):
        self.size = max_size
        self.queue = [None] * max_size
        self.front = -1
        self.rear = -1

    def clearQ(self):
        self.front = self.rear = -1

    def isFullQ(self):
        return self.rear == self.size - 1

    def isEmptyQ(self):
        return self.front == -1 or self.front > self.rear

    def enQ(self, value):
        if self.isFullQ():
            print("Queue Overflow.")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = value

    def deQ(self):
        if self.isEmptyQ():
            print("Empty Queue.")
            return None
        else:
            value = self.queue[self.front]
            self.front += 1
            if self.front > self.rear:
                self.clearQ()
            return value

    def displayQ(self):
        if self.isEmptyQ():
            print("Queue is empty.")
        else:
            print("front ->", end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print("<- rear")

q = QueueArray(3)
q.clearQ()
q.enQ(100)
q.enQ(200)
q.enQ(300)
q.displayQ()
x = q.deQ()
q.displayQ()
x = q.deQ()
q.displayQ()
x = q.deQ()
q.displayQ()
x = q.deQ()