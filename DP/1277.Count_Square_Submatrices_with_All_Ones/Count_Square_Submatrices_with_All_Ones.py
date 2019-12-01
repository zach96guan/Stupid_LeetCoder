class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # dp
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0: 
                    continue
                    
                side = min(matrix[i - 1][j], matrix[i][j - 1])
                matrix[i][j] = side + 1 if matrix[i - side][j - side] else side
                
        return sum(x for row in matrix for x in row)
    