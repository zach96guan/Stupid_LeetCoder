"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        # one-pass, O(N)
        dummy = Node(insertVal, head)
        
        # corner case
        if not head:
            head = dummy
            head.next = dummy
            return head
         
        cur = head
        while True:
            if cur.next.val < cur.val and (insertVal <= cur.next.val or insertVal >= cur.val):
                break
            elif cur.val <= insertVal <= cur.next.val:
                break
            elif cur.next == head:
                break
            
            cur = cur.next
        
        dummy.next, cur.next = cur.next, dummy
        return head
        
        