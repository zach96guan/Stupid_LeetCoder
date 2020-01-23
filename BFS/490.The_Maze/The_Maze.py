class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # bfs
        m, n = len(maze), len(maze[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        q = [start]
        while q:
            i, j = q.pop(0)

            if [i, j] == destination:
                return True
            
            maze[i][j] = 2
            
            for di, dj in dirs:
                tmp_i, tmp_j = i, j
                while 0 <= tmp_i + di < m and 0 <= tmp_j + dj < n and maze[tmp_i + di][tmp_j + dj] != 1:
                    tmp_i += di
                    tmp_j += dj
                
                if maze[tmp_i][tmp_j] == 0:
                    q.append([tmp_i, tmp_j])
        
        return False
        