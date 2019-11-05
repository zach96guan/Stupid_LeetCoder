# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        # dfs + bfs, O(N), O(N)
        def dfs(root, parent):
            if not root:
                return     
            root.parent = parent
            dfs(root.left, root)
            dfs(root.right, root)
        
        dfs(root, None)
        
        q = [(target, 0)]
        vis = {target}
        while q:
            for _ in range(len(q)):
                node, d = q.pop(0)
                if d == K:
                    ret = [node.val]
                    for o, _ in q:
                        ret.append(o.val)
                    return ret

                for next_node in [node.parent, node.left, node.right]:
                    if next_node and next_node not in vis:
                        q.append((next_node, d + 1))
                        vis.add(next_node)
        return []
