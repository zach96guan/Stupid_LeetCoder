class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre[i][j] = mat[i - 1][j - 1] + pre[i - 1][j] + pre[i][j - 1] - pre[i - 1][j - 1]
        
        ret = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1 = max(i - K, 0)
                r2 = min(i + K, m - 1)
                c1 = max(j - K, 0)
                c2 = min(j + K, n - 1)
                r1 += 1; r2 += 1; c1 += 1; c2 += 1
                
                ret[i][j] = pre[r2][c2] - pre[r2][c1 - 1] - pre[r1 - 1][c2] + pre[r1 - 1][c1 - 1]
        
        return ret
        