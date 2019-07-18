class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # binary search
        # O(1) worst O(logN), O(1)

        missing = lambda x: nums[x] - nums[0] - x
        n = len(nums)
        
        if missing(n-1) < k:
            return nums[-1] + k - missing(n-1)
        
        l, r = 0, n-1
        while l < r:
            m = l + r >> 1
            if missing(m) < k:
                l = m + 1
            else:
                r = m
        return nums[l-1]+ k - missing(l-1)