class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # recursion
        rows = [] 
        
        def helper(i, j):
            if j == 0 or i == j:
                return 1
            return rows[i - 1][j] + rows[i - 1][j - 1]
            
        for i in range(rowIndex + 1):
            tmp = []
            for j in range(i + 1):
                tmp.append(helper(i, j))
            rows.append(tmp)
        
        return rows[rowIndex]
        