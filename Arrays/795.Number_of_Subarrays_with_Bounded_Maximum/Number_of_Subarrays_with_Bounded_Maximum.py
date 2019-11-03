class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        # counting, O(N), O(1)
        def count(bound):
            ret = cur = 0
            for a in A:
                cur = cur + 1 if a <= bound else 0
                ret += cur
            return ret
        
        return count(R) - count(L - 1)
    