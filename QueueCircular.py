class CircularQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.front = -1
        self.rear = -1

    def isempty(self):
        return self.front == -1

    def isfull(self):
        return (self.rear + 1) % self.max_size == self.front

    def enQ(self, value):
        if self.isfull():
            print("Queue Overflow: Cannot enQ, queue is full.")
        else:
            if self.isempty():
                self.front = 0
            self.rear = (self.rear + 1) % self.max_size
            self.queue[self.rear] = value
            print(f"enQd: {value}")

    def deQ(self):
        if self.isempty():
            print("Queue Underflow: Cannot deQ, queue is empty.")
            return None
        else:
            value = self.queue[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.max_size
            print(f"deQd: {value}")
            return value

    def display(self):
        if self.isempty():
            print("Queue is empty.")
        else:
            print("Queue elements are:", end=" ")
            i = self.front
            while True:
                print(self.queue[i], end=" ")
                if i == self.rear:
                    break
                i = (i + 1) % self.max_size
            print()

cq = CircularQueue(5)

cq.enQ(10)
cq.enQ(20)
cq.enQ(30)
cq.enQ(40)
cq.enQ(50)
cq.display()

cq.enQ(60) 

cq.deQ()
cq.deQ()
cq.display()

cq.enQ(60)
cq.enQ(70)
cq.display() 

cq.deQ()
cq.deQ()
cq.deQ()
cq.deQ()
cq.deQ()
cq.deQ() 