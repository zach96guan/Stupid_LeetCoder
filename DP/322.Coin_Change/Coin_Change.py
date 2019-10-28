class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for a in range(1, amount + 1):
            for coin in coins:
                if a >= coin:
                    dp[a] = min(dp[a], dp[a - coin] + 1)
        
        return dp[-1] if dp[-1] < float('inf') else -1
    