class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # dp
        total = sum(nums)
        if total & 1 != 0:
            return False 
        
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
    
        for num in nums:
            for i in range(target, num - 1, -1):
                if dp[target]: 
                    return True
                
                dp[i] = dp[i] or dp[i - num]
                
        return dp[-1]
        