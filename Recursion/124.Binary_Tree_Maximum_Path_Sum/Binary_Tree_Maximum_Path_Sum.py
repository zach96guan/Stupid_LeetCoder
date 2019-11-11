# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # O(N)
        self.ret = float('-inf')
        self.dfs(root)
        return self.ret
    
    
    def dfs(self, root):
        if not root:
            return 0
        
        l = max(self.dfs(root.left), 0)
        r = max(self.dfs(root.right), 0)
        
        self.ret = max(self.ret, l + r + root.val)
        return max(l, r) + root.val
        