class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy
        ret = 0
        for i, num in enumerate(nums):
            if ret < i:
                return False
            else:
                ret = max(ret, i + num)
        
        return True
        