# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # iteration, O(N)
        if not root:
            return []

        stack = [root]
        ret = []

        while stack:
            cur = stack.pop()
            ret.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
                
        return ret[::-1]
    