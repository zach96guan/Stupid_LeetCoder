class Solution:
    # Reservoir Sampling
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        
    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        ret = -1
        cnt = 0
        
        for i, num in enumerate(self.nums):
            if num == target:
                cnt += 1
                if random.randint(1, cnt) == cnt:
                    ret = i
        return ret
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)