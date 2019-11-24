class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ret = 0
        
        for i in range(m):
            if grid[i][0] == 0:
                self.dfs(grid, i, 0)
            if grid[i][-1] == 0:
                self.dfs(grid, i, n - 1)
                
        for j in range(n):
            if grid[0][j] == 0:
                self.dfs(grid, 0, j)
            if grid[-1][j] == 0:
                self.dfs(grid, m - 1, j)
                
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    self.dfs(grid, i, j)
                    ret += 1
        return ret
    
    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 1:
            return
        
        grid[i][j] = 1
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)
        
        