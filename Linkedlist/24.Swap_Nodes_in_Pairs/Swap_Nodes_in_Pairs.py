# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # from pre -> a -> b -> b.next to pre -> b -> a -> b.next
        dummy = ListNode(0)
        pre = dummy
        pre.next = head
        
        while pre.next and pre.next.next:
            tmp_a = pre.next
            tmp_b = pre.next.next
            
            pre.next, tmp_b.next, tmp_a.next = tmp_b, tmp_a, tmp_b.next
            pre = tmp_a
            
        return dummy.next
    