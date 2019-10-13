# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        # f1: rob, f2: not rob
        # pre: f2(cur) = f1(cur.left) + f1(cur.right)
        # cur: f1(cur) = max(cur.val + f2(cur.left) + f2(cur.right), f2(cur))
        # return pre, cur
        return self.dfs(root)[1]
    

    def dfs(self, root):
        if not root:
            return 0, 0
        
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        
        return l[1] + r[1], max(root.val + l[0] + r[0], l[1] + r[1])
        