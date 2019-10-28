# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # binary search, O(log^2(N)) == O(h^2)
        if not root:
            return 0
        
        l = self.get_height(root.left)
        r = self.get_height(root.right)
        
        if l == r:
            return 2 ** l + self.countNodes(root.right)
        else:
            return 2 ** r + self.countNodes(root.left)
    
    
    def get_height(self, root):
        if not root:
            return 0
        return self.get_height(root.left) + 1
        