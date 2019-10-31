class Solution:
    def minWindow(self, S: str, T: str) -> str:
        # dp, O(M*N)
        m, n = len(S), len(T)
        if m < n:
            return ""
        
        dp = [[0] * n for _ in range(m)]  # m * n
        
        # find the subsequence start index
        for i in range(m):
            if S[i] == T[0]:
                dp[i][0] = i
            else:
                if i == 0:
                    dp[i][0] = -1
                else:
                    dp[i][0] = dp[i - 1][0]
        
        # initialize all dp[0][j] (j != 0) to -1
        for j in range(1, n):
            dp[0][j] = -1
            for i in range(1, m):
                if S[i] == T[j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        l, min_len = 0, m + 1
        for i in range(n - 1, m):
            if dp[i][-1] != -1:
                if i - dp[i][-1] + 1 < min_len:
                    min_len = i - dp[i][-1] + 1
                    l = dp[i][-1]
        
        return S[l:l + min_len] if min_len < m + 1 else ""
        