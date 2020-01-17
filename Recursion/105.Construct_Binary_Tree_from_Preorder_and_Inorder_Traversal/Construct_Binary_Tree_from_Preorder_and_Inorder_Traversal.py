# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder.pop(0))
        pos = inorder.index(root.val)
        
        root.left = self.buildTree(preorder, inorder[:pos])
        root.right = self.buildTree(preorder, inorder[pos + 1:])
        
        return root
        