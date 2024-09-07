class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None

class Solution:
    def __init__(self) -> None:
        self.root = Node(5)
        self.root.next = Node(10)
        self.root.next.next = Node(15)
        self.root.next.next.next = Node(20)
        self.root.next.next.next.next = Node(25)
        self.root.next.next.next.next.next = Node(30)
        
    # ll traversal
    def traverse(self,root):
        while root:
            print(root.val ,end=' ')
            root = root.next
            
    # find mid (fast and slow pointer)
    # 1->2->3->4->5->6->7
    # 5,10,15,20,25,30
    def findmid(self,root):
        slow = fast = root
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.val)
        
    def reverse(self,root):
        # 1->2->3->4->5
        prev = Node(None)
        curr = root
        next = root.next
        
        while prev:
            curr.next = prev
            prev = curr
            curr = curr.next
            next = curr.next
        print('hi')
        self.traverse(prev)
            
            
            
        
        
    
s = Solution()
# s.traverse(s.root)
# s.findmid(s.root)
s.reverse(s.root)

    
