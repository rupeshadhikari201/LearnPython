class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
"""
        1
       / \
      2   3
     / \ / \
    4   56  7

Preorder  : (root,left,right)   => 1,2,4,5,3,6,7
Inorder   : (left,root,right)   => 4,2,5,1,6,3,7
Postorder : (left,right,root)   => 4,5,2,6,7,3,1
"""   
  
class Tree: 
    def __init__(self):
        self.root = Node(1)
        self.root.left = Node(2)
        self.root.right = Node(3)
        self.root.left.left = Node(4)
        self.root.left.right = Node(5)
        self.root.right.left = Node(6)
        self.root.right.right = Node(7)
        
    def preorder(self,root):
        if root == None:
            return 
        print(root.value, end = ' ')
        self.preorder(root.left)
        self.preorder(root.right)
    
    def inorder(self, root):
        if root == None:
            return 
        self.inorder(root.left)
        print(root.value, end = ' ')
        self.inorder(root.right)
    
    def postorder(self, root):
        if root == None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.value, end = ' ')    
        
tree = Tree()
print("\nThe preorder traversal is : ")
tree.preorder(tree.root)
print("\nThe inorder traversal is : ")
tree.inorder(tree.root)
print("\nThe postorder traversal is : ")
tree.postorder(tree.root)
