class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # bfs
        m, n = len(grid), len(grid[0])
        
        if m <= 1 and n <= 1:  # corner case
            return 0

        q = [(0, 0, 0, 0)]
        vis = {(0, 0, 0)}
        
        while q:
            i, j, cur, t = q.pop(0)

            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n:
                    tmp = cur + grid[ni][nj]
                    if tmp > k:
                        continue
                    
                    if ni == m - 1 and nj == n - 1:
                        return t + 1

                    if (ni, nj, tmp) not in vis:               
                        q.append((ni, nj, tmp, t + 1))
                        vis.add((ni, nj, tmp))

        return -1
    
    