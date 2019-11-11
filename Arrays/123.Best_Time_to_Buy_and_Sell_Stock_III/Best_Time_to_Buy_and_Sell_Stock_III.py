class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # forward
        max_profit = 0
        min_price = float('inf')
        tmp_profits = []
        for p in prices:
            min_price = min(min_price, p)
            max_profit = max(max_profit, p - min_price)
            tmp_profits.append(max_profit)
        
        # backward
        max_profit = 0
        max_price = float('-inf')
        ret = 0
        for i in range(len(prices))[::-1]:
            p = prices[i]
            max_price = max(max_price, p)
            max_profit = max(max_profit, max_price - p)
            ret = max(ret, tmp_profits[i] + max_profit)
        
        return ret
        