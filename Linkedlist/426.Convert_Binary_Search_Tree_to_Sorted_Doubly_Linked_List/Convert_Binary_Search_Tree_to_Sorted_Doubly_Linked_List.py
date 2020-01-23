"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # O(N)
        if not root:
            return root
        
        # in-order
        pre = self.treeToDoublyList(root.left)
        nxt = self.treeToDoublyList(root.right)
        
        head = tail = root
        # connect nxt
        if nxt:
            tail = nxt.left
            root.right = nxt
            nxt.left = root
        # connect pre
        if pre:
            head = pre
            root.left = pre.left
            pre.left.right = root
        
        # link head/tail
        head.left = tail
        tail.right = head
        
        return head      
        