# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # O(H + k), O(H + k)
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            
            if k == 0:
                return root.val
            else:
                root = root.right
        
        # follow-up -> O(H) for insert/delete, O(k) for search
        # use doubly-linked list
    