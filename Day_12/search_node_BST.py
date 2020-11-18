'''
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''
class BST:
    def search(self, node, data):
        if node==None:
            return False
        if node.data==data:
            return True
        elif node.data<data:
            return self.search(node.right,data)
        else:
            return self.search(node.left,data)

class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Tree:
    def createNode(self, data):
        return Node(data)
    
    def insert(self, node, data):
        if node is None:
            return self.createNode(data)
        else:
            if data < node.data:
                node.left = self.insert(node.left, data)
            else:
                node.right = self.insert(node.right, data)
            return node

    def traverseInorder(self, root):
        if root is not None:
            print(root.data, end= " ")
            self.traverseInorder(root.left)
            self.traverseInorder(root.right)
    
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr = input().strip().split()
        root = None
        tree = Tree()
        root = tree.insert(root, int(arr[0]))
        for j in range(1, n):
            root = tree.insert(root, int(arr[j]))
        #tree.traverseInorder(root)
        num = int(input())
        find = BST()
        if find.search(root, num):
            print(1)
        else:
            print(0)