class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] = min(dp[a], dp[a - coin] + 1)
        
        return dp[-1] if dp[-1] < float('inf') else -1
        