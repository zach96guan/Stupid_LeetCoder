class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # find smallest leftmost chunk
        # O(N), O(1)
        ret = cur = 0
        for i, x in enumerate(arr):
            cur = max(cur, x)
            if i == cur:
                ret += 1
                
        return ret
    