class TreeNode:
    def __init__(self, data):
        self.data = data
        self.LLink = None
        self.RLink = None
class Tree:
    def __init__(self):
        self.root = None
    def insert(self, root, data):
        if root is None:
            return TreeNode(data)
        if data < root.data:
            root.LLink = self.insert(root.LLink, data)
        else:
            root.RLink = self.insert(root.RLink, data)
        return root
    def inorder(self, root):
        if root:
            self.inorder(root.LLink)
            print(root.data, end=" ")
            self.inorder(root.RLink)
    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.LLink)
            self.preorder(root.RLink)
    def postorder(self, root):
        if root:
            self.postorder(root.LLink)
            self.postorder(root.RLink)
            print(root.data, end=" ")
    def minValueNode(self, node):
        current = node
        while current.LLink is not None:
            current = current.LLink
        return current
    def delete(self, value):
        def deleteRecursive(root, data):
            if root is None:
                return root
            if data < root.data:
                root.LLink = deleteRecursive(root.LLink, data)
            elif data > root.data:
                root.RLink = deleteRecursive(root.RLink, data)
            else:
                if root.LLink is None:
                    return root.RLink
                elif root.RLink is None:
                    return root.LLink
                temp = self.minValueNode(root.RLink)
                root.data = temp.data
                root.RLink = deleteRecursive(root.RLink, temp.data)
            return root
        self.root = deleteRecursive(self.root, value)
    def dfs(self, root, target):
        if root is None:
            return False
        if root.data == target:
            return True
        return self.dfs(root.LLink, target) or self.dfs(root.RLink, target)
    def bfs(self, target):
        if self.root is None:
            return False
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.data == target:
                return True
            if node.LLink:
                queue.append(node.LLink)
            if node.RLink:
                queue.append(node.RLink)
        return False
bst = Tree()
bst.root = bst.insert(bst.root, 15)
bst.insert(bst.root, 9)
bst.insert(bst.root, -2)
bst.insert(bst.root, 10)
bst.insert(bst.root, 20)
bst.insert(bst.root, 19)
bst.insert(bst.root, 30)
bst.delete(19)
print("Preorder:")
bst.preorder(bst.root)
print("\nPostorder:")
bst.postorder(bst.root)
print("\nInorder:")
bst.inorder(bst.root)

print("\nDFS Search for 10:", bst.dfs(bst.root, 10))
print("BFS Search for 10:", bst.bfs(10))