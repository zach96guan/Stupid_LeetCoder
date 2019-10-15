class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        # bfs twice
        n = len(A)
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def find_island():
            for i in range(n):
                for j in range(n):
                    if A[i][j] == 1:
                        return i, j
        
        def nei(x, y):
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    yield nx, ny
        
        # bfs to find zeros
        a, b = find_island()
        q = [(a, b)]
        vis = {(a, b)}
        zeros = []
        while q:
            x, y = q.pop(0)
            for nx, ny in nei(x, y):
                if (nx, ny) not in vis:
                    vis.add((nx, ny))
                    if A[nx][ny] == 0:
                        zeros.append((nx, ny))
                    else:
                        q.append((nx, ny))
        
        # bfs to find the second island
        ret = 0
        while zeros:
            ret += 1
            size = len(zeros)
            for _ in range(size):
                x, y = zeros.pop(0)
                for nx, ny in nei(x, y):
                    if (nx, ny) not in vis:
                        vis.add((nx, ny))
                        if A[nx][ny] == 1:
                            return ret
                        else:
                            zeros.append((nx, ny))
        
        return ret
            