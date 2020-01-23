# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        # O(N), recursion
        self.lca = None
        self.deepest = 0

        
        def helper(node, depth):
            self.deepest = max(self.deepest, depth)
            if not node:
                return depth
            
            l = helper(node.left, depth + 1)
            r = helper(node.right, depth + 1)
            
            if l == r == self.deepest:
                self.lca = node
            
            return max(l, r)
        
        
        helper(root, 0)
        return self.lca
    