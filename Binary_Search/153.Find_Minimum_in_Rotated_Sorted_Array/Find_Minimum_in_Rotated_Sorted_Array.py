class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        
        while l < r:
            m = l + r >> 1
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        return nums[l]
        