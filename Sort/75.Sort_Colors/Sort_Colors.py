class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # O(N), O(1)
        pos0 = pos1 = 0
        
        for i, num in enumerate(nums):
            tmp = num
            nums[i] = 2
            
            if num <= 1:
                nums[pos1] = 1
                pos1 += 1
                
            if num == 0:
                nums[pos0] = 0
                pos0 += 1
        