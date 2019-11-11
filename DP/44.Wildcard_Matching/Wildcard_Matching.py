class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp, O(M * N)
        m, n = len(s), len(p)

        dp = [[False] * (m + 1) for _ in range(n + 1)]  # N * M
        dp[0][0] = True
        
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                j = 1
                while j <= m and not dp[i - 1][j - 1]:  # find previous match
                    j += 1
                dp[i][j - 1] = dp[i - 1][j - 1]
                while j <= m:
                    dp[i][j] = True
                    j += 1
            
            elif p[i - 1] == '?':
                for j in range(1, m + 1):
                    dp[i][j] = dp[i - 1][j - 1]
            
            else:
                for j in range(1, m + 1):
                    dp[i][j] = dp[i - 1][j - 1] and p[i - 1] == s[j - 1]
        
        return dp[-1][-1]
        