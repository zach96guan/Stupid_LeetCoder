class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # bfs
        m, n = len(grid), len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        q = [(0, 0, 0)]
        costs = {}
        
        while q:
            nx, ny, cost = q.pop(0)
            while 0 <= nx < m and 0 <= ny < n and (nx, ny) not in costs:
                costs[(nx, ny)] = cost
                
                for dx, dy in dirs:
                    q.append((nx + dx, ny + dy, cost + 1))
                    
                dx, dy = dirs[grid[nx][ny] - 1]
                nx += dx
                ny += dy
                        
        return costs[m - 1, n - 1]
        
        