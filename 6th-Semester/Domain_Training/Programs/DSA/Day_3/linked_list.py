class Node:
    def __init__(self,data):
        self.data = str(data)
        self.left = None
        self.right = None
        print(f"Node created with value {self.data}")

a = Node('10')
b = Node('20')
c = Node('30')

