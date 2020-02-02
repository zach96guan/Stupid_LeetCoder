# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        # O(H)
        mod = 10 ** 9 + 7
        self.total_sum = 0
        self.ret = float('-inf')
        
        def helper(node):
            if node:
                self.total_sum += node.val
                helper(node.left)
                helper(node.right)
        
        def dfs(node):
            if node:
                tmp1 = node.val + dfs(node.left) + dfs(node.right)
                tmp2 = self.total_sum - tmp1
                self.ret = max(self.ret, tmp1 * tmp2)
                return tmp1
            return 0
        
        helper(root)
        dfs(root)
        
        return self.ret % mod
        
        