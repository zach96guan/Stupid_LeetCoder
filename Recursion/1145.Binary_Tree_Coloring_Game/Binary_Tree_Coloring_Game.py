# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        # left/right/parent subtree
        cnt = [0, 0, 0]
        
        def count(node):
            if not node:
                return 0
            
            l, r = count(node.left), count(node.right)
            if node.val == x:
                cnt[0], cnt[1] = l, r
            
            return l + r + 1
        
        count(root)
        cnt[-1] = n - cnt[0] - cnt[1] - 1
        
        return max(cnt) > n >> 1
        