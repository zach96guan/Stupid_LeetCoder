class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix) == 0:
            return False
        
        m, n = len(matrix), len(matrix[0])
        r, c = m - 1, 0
        
        while r >= 0 and c <= n - 1:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                c += 1
            else:
                r -= 1
            
        return False
        