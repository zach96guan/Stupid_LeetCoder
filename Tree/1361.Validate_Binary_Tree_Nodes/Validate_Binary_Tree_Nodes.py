class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        children = 0
        for l, r in zip(leftChild, rightChild):
            if l != -1:
                children += 1
            if r != -1:
                children += 1
        
        return children == n - 1
        