# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        # dfs
        if not root:
            return []
        
        q = [root.val]
        
        def dfs(root, is_left, is_right):
            if not root:
                return
            
            if is_left or (not root.left and not root.right):
                q.append(root.val)
            
            if root.left and root.right:
                dfs(root.left, is_left, False)
                dfs(root.right, False, is_right)
            else:
                dfs(root.left, is_left, is_right)
                dfs(root.right, is_left, is_right)
            
            if is_right and (root.left or root.right):
                q.append(root.val)
        
        
        dfs(root.left, True, False)
        dfs(root.right, False, True)
        
        return q
        
        