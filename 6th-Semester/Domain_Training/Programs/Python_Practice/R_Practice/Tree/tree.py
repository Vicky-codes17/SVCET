class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
     self.root = None

    def insert(self,data):
        z = Node(data)
        if self.root is None:
            self.root = z
            return
        temp = self.root
        while True:
            if data<temp.data:
                if temp.left is None:
                    temp.left = z
                    break
                else:
                    temp = temp.left
            else:
                if temp.right is None:
                    temp.right = z
                    break
                else:
                    temp = temp.right
    
    def inorder(self, node):
        if node:
         self.inorder(node.left)
         print(node.data, end=" ")
         self.inorder(node.right)

    def preorder(self, node):
        if node:
         print(node.data, end=" ")
         self.preorder(node.left)
         self.preorder(node.right)

    def postorder(self, node):
        if node:
         self.postorder(node.left)
         self.postorder(node.right)
         print(node.data, end = " ")
if __name__ == "__main__":
    x = Tree()
    x.insert(100)
    x.insert(70)
    x.insert(110)
    x.insert(60)
    x.insert(65)
    x.insert(77)
    x.insert(10)
    x.insert(50)
    x.insert(112)
    x.insert(63)

    x.inorder(x.root)
    print()
    x.preorder(x.root)
    print()
    x.postorder(x.root)
    