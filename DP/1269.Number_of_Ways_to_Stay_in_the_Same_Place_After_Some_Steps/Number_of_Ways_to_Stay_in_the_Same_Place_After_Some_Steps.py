class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10 ** 9 + 7
        n = min(arrLen, steps)
        
        dp = [[0] * n for _ in range(steps + 1)]
        dp[0][0] = 1
        
        for i in range(1, steps + 1):
            for j in range(n):
                dp[i][j] = dp[i - 1][j]
                
                if j > 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % mod
                
                if j < n - 1:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j + 1]) % mod
        
        return dp[-1][0]
    
    