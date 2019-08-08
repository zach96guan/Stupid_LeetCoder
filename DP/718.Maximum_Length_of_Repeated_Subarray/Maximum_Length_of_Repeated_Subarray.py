class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # O(M*N), O(M*N)
        dp = [[0] * (len(B)+1) for _ in range(len(A)+1)]
        
        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1

        return max(max(dp[i]) for i in range(len(dp)))
    