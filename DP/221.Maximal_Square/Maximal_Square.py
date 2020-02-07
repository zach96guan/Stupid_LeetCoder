class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp, O(M * N)
        if not matrix or len(matrix) == 0:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        ret = 0
        
        for i in range(m):
            for j in range(n):
                if not i or not j:
                    dp[i][j] = int(matrix[i][j])
                
                elif matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                
                ret = max(ret, dp[i][j])
        
        return ret ** 2
        