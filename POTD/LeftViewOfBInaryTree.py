'''
          1
       /     \
     2        3
   /   \     / \
 4      5   6    7
   \
    8   
   /
  12
Left View of Binary Tree : 1,2 3, 8
'''

class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
    
class Tree:
    def __init__(self) -> None:
        self.root = Node(1)
        self.root.left = Node(2)
        self.root.right = Node(3)
        self.root.left.left = Node(4)
        self.root.left.right = Node(5)
        self.root.right.left = Node(6)
        self.root.right.right = Node(7)
        self.root.left.left.left = Node(8)
        
    def LeftView(self,root):
        ans = []
        if root == None:
            return 
            
        self.LeftView(root.left)
        ans.append(root.value)
        self.LeftView(root.right)
    
tree  = Tree()
ans = tree.LeftView(tree.root)
print(ans)