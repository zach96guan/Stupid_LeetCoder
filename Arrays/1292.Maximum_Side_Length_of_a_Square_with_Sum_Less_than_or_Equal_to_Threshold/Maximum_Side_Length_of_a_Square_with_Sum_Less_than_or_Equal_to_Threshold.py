class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        # prefix sum + binary search
        m, n = len(mat), len(mat[0])
        
        l, r = 0, min(m, n)
        while l < r:
            m = l + r + 1 >> 1
            if self.check_sum(mat, m, threshold):
                l = m
            else:
                r = m - 1
        return l


    def check_sum(self, mat, k, threshold):
        m, n = len(mat), len(mat[0])
        temp_sum = [[0] * n for _ in range(m)]

        for j in range(n):
            tmp = 0
            for i in range(k):
                tmp += mat[i][j]
            temp_sum[0][j] = tmp

            for i in range(1, m - k + 1):
                tmp += mat[i + k - 1][j] - mat[i - 1][j]
                temp_sum[i][j] = tmp

        for i in range(m - k + 1):
            tmp = 0
            for j in range(k):
                tmp += temp_sum[i][j]

            if tmp <= threshold:
                return True

            for j in range(1, n - k + 1):
                tmp += temp_sum[i][j + k - 1] - temp_sum[i][j - 1]
                if tmp <= threshold:
                    return True
        
        return False
    
    