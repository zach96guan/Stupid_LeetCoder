# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        # dfs
        self.ret = 0
        self.dfs(root, None, None)
        return self.ret
    
    def dfs(self, node, parent, grandparent):
        if not node:
            return
        if grandparent and grandparent.val & 1 == 0:
            self.ret += node.val
        
        self.dfs(node.left, node, parent)
        self.dfs(node.right, node, parent)
        
        