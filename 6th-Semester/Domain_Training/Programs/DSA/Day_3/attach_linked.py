
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        print("Node created with values ",self.data)

root = Node(20)
root.left = Node(10)
root.right = Node(30)

# Another Level 
root.left.left = Node(8)

# root = Node('Vignesh')
# root.left = Node('Viki')
# root.right = Node('Ramesh')

# Swap of left and right
root.left, root.right = root.right, root.left
        
print(root.left.left,root.left.data,root.data,root.right.data)
