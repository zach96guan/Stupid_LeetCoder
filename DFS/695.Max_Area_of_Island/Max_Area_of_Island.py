class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ret = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ret = max(ret, self.dfs(grid, i, j))
        return ret
    
    
    def dfs(self, grid, i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
            grid[i][j] = 0
            return self.dfs(grid, i - 1, j) + self.dfs(grid, i + 1, j) + self.dfs(grid, i, j - 1) + self.dfs(grid, i, j + 1) + 1
        return 0
        