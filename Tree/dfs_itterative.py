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
df sds
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
        stack  = []
        current = root
        while stack or current:
            while current:
                print(current.value, end = ' ')
                stack.append(current)
                current = current.left
            current = stack.pop()
            current = current.right   
              
    def inorder(self, root):
        stack = []
        current = root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            print(current.value, end=' ')
            current = current.right
    
    def postorder(self, root):
        stack1 = [root]
        stack2 = []
        while stack1:
            current = stack1.pop()
            stack2.append(current)
            
            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)
        while stack2:
            current = stack2.pop()
            print(current.value, end=' ')
               
        
tree = Tree()
print("\nThe Iterative preorder traversal is : ")
tree.preorder(tree.root)
print("\nThe Iterative inorder traversal is : ")
tree.inorder(tree.root)
print("\nThe Iterative postorder traversal is : ")
tree.postorder(tree.root)
