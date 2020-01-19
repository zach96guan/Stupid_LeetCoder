class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        pos = 0
        
        for i, num in enumerate(nums[1:], 1):
            while i > nums[pos] + pos:
                pos += 1
            dp[i] = dp[pos] + 1
        
        return dp[-1]
        