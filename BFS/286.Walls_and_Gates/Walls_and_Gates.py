class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # bfs
        if not rooms:
            return rooms
        
        m, n = len(rooms), len(rooms[0])
        q = []
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))
        
        while q:
            for _ in range(len(q)):
                i, j = q.pop(0)

                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and rooms[ni][nj] == 2 ** 31 - 1:
                        rooms[ni][nj] = rooms[i][j] + 1
                        q.append((ni, nj))

        