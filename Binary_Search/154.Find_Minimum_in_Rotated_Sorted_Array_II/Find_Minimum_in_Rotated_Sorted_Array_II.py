class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        
        while l < r:
            while l < r and nums[l] == nums[l + 1]:
                l += 1
            while l < r and nums[r] == nums[r - 1]:
                r -= 1
                
            m = l + r >> 1
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        return nums[l]
        