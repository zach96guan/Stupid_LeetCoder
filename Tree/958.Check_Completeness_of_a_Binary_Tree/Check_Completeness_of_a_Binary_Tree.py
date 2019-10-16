# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        # O(N), O(N)
        bfs = []
        bfs.append(root)
        
        i = 0
        cur = bfs[i]
        while cur:
            bfs.append(cur.left)
            bfs.append(cur.right)
            i += 1
            cur = bfs[i]
        
        return not any(bfs[i:])
        