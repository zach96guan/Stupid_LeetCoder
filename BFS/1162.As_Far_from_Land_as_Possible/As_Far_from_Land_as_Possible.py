class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # bfs
        n = len(grid)
        bfs = []
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs.append((i, j))
        
        ret = -1
        while bfs and len(bfs) < n * n:  # avoid all 1s
            tmp = []
            for i, j in bfs:
                for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 0:
                        tmp.append((ni, nj))
                        grid[ni][nj] = 1
            bfs = tmp
            ret += 1
        
        return ret
        