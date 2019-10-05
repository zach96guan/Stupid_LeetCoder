class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # dp, O(N^2), O(N^2)
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        for l in range(len(s) - 1, -1, -1):
            dp[l][l] = 1
            for r in range(l + 1, n):
                if s[l] == s[r]:
                    dp[l][r] = dp[l + 1][r - 1] + 1 + 1
                else:
                    dp[l][r] = max(dp[l + 1][r], dp[l][r - 1])
        
        return dp[0][-1]
 