class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # O(M*N)
        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        hist = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    hist[i][j] = hist[i - 1][j] + 1
                    
        return max(self.largestRectangleArea(r) for r in hist)
    
    
    def largestRectangleArea(self, heights):
        # referring to lc84
        heights.append(0)
        stack = [-1] 
        ret = 0
        
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ret = max(ret, h * w)
            
            stack.append(i)
        
        heights.pop()
        return ret

    