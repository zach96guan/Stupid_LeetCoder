"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # O(N), O(1)
        if not root:
            return root
        
        dummy = Node(-1)
        dummy.next = root
        
        while root.left:
            level = root.left
            
            cur = None
            while root:
                root.left.next = root.right
                cur, root = root.right, root.next
                if cur and root:
                    cur.next = root.left
            
            root = level
        
        return dummy.next
            