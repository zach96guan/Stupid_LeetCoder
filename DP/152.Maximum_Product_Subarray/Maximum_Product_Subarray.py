class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = minp = maxp = nums[0]
        
        for num in nums[1:]:
            candi = (num, num * minp, num * maxp)
            minp, maxp = min(candi), max(candi)
            
            ret = max(ret, maxp)
            
        return ret
    