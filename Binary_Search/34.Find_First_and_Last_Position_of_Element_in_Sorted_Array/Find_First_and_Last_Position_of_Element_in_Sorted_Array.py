class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # log(N), O(1)
        n = len(nums)
        ret1 = ret2 = -1
        
        if not nums or n == 0:
            return ret1, ret2
        
        # find first
        l, r = 0, n - 1
        while l < r:
            m = l + r >> 1
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        if nums[l] != target:
            return ret1, ret2
        ret1 = l
        
        # find last
        r = n - 1
        while l < r:
            m = l + r + 1 >> 1  # keep mid in rightmost
            if nums[m] <= target:
                l = m
            else:
                r = m - 1
        ret2 = l
        
        return ret1, ret2
        