class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(N), O(1)
        ret = tmp = 0
        
        for i in range(len(nums)):
            if i > 0 and nums[i] <= nums[i - 1]:
                tmp = i
            
            ret = max(ret, i - tmp + 1)
        
        return ret
        