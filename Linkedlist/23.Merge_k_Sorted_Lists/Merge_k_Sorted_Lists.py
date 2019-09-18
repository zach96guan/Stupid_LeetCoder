# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # O(NlogK), O(N)
        # K is number of linked lists, N is number of nodes in final linked list.
        q = []   
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(q, (l.val, i, l))  # for heap comparison
        
        dummy = ListNode(0)
        cur = dummy
        while q:
            _, i, node = heapq.heappop(q)
            cur.next = node
            cur = cur.next
            
            node = node.next
            if node:
                heapq.heappush(q, (node.val, i, node))

        return dummy.next
        