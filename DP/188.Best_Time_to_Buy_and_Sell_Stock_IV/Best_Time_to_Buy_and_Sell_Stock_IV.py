class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # O(N * k)
        if not prices or len(prices) <= 1:
            return 0
        
        n = len(prices)
        if k >= n // 2:
            return self.stock2(prices)
        
        dp = collections.defaultdict(int)
        for i in range(1, k + 1):
            max_price = -prices[0]
            for j in range(1, n):
                dp[i, j] = max(dp[i, j - 1], prices[j] + max_price)
                max_price = max(max_price, dp[i - 1, j - 1] - prices[j])
        
        return dp[k, n - 1]
    
    
    def stock2(self, prices):
        ret = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                ret += prices[i] - prices[i - 1]
        return ret
    