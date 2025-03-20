class ArrayList:
    def __init__(self):
        self.items = []
    def add(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return len(self.items) == 0
    def clear(self):
        self.items = []
class Vertex:
    def __init__(self, data=None):
        self.data = data
        self.visited = False
        self.inStack = False
    def getVisit(self):
        return self.visited
class Graph:
    def __init__(self, s):
        self.size = s
        self.list = [None] * s
        self.adjMatrix = [[0] * s for _ in range(s)]
        self.count = 0
        self.stack = ArrayList()
    def addVertex(self, data):
        self.list[self.count] = Vertex(data)
        self.count += 1
    def addEdge(self, start, end):
        self.adjMatrix[start][end] = 1
    def removeEdge(self, start, end):
        self.adjMatrix[start][end] = 0
    def show(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.adjMatrix[i][j], end=' ')
            print()
    def dfs(self, start):
        self.stack.clear()
        self.stack.add(start)
        while not self.stack.isEmpty():
            x = self.stack.pop()
            if not self.list[x].visited:
                print(self.list[x].data)
                self.list[x].visited = True
                for i in range(self.size):
                    if self.adjMatrix[x][i] == 1 and not self.list[i].visited:
                        self.stack.add(i)
g = Graph(4)
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addEdge(0, 2)
g.removeEdge(0,2)
g.addEdge(0, 3)
g.addEdge(1, 0)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.show()
print("D F S : ")
g.dfs(1)
