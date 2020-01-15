class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        """
        1. If you pick piles[i], your result will be piles[i] - dp[i + 1][j]
        2. If you pick piles[j], your result will be piles[j] - dp[i][j - 1]
        """
        # dp[i][j] means the biggest number of stones you can get more than opponent picking piles in piles[i] ~ piles[j]
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n): 
            dp[i][i] = piles[i]
            
        for d in range(1, n):
            for i in range(n - d):
                dp[i][i + d] = max(piles[i] - dp[i + 1][i + d], piles[i + d] - dp[i][i + d - 1])
        
        return dp[0][-1] > 0
    
    
#         dp = [0] * len(piles)      
#         for i in range(1, len(piles)):
#             for j in range(len(piles) - i):
#                 dp[j] = max(piles[j] - dp[j + 1], piles[j + i] - dp[j])
        
#         return dp[0] > 0
