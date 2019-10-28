# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # O(N), bottom-up
        return self.helper(root)[0]
    
    
    def helper(self, root):
        if not root:
            return True, -1
        
        l_flag, l_height = self.helper(root.left)
        r_flag, r_height = self.helper(root.right)

        if not l_flag:
            return False, -1
        if not r_flag:
            return False, -1
        
        return abs(l_height - r_height) < 2, max(l_height, r_height) + 1
        