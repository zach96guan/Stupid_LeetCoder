class Solution:
    def orangesRotting(self, grid: 'List[List[int]]') -> 'int':
        # bfs, O(N), O(N)
        stack = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    stack.append((i, j, 0))
        
        t = 0
        while stack:
            x, y, t = stack.pop(0)
            for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    stack.append((nx, ny, t+1))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return t
