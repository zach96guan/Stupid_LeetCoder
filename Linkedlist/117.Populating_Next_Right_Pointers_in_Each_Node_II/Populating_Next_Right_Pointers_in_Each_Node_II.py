"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        dummy = tmp = Node(-1)
        ret = root
        
        while root:
            while root:
                if root.left:
                    tmp.next = root.left
                    tmp = tmp.next
                    
                if root.right:
                    tmp.next = root.right
                    tmp = tmp.next
                    
                root = root.next
                
            root = dummy.next
            tmp = dummy
            dummy.next = None
            
        return ret
        