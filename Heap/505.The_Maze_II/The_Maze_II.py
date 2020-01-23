class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        # priority queue
        m, n = len(maze), len(maze[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        q = [(0, start[0], start[1])]
        stopped = {(start[0], start[1]): 0}
        
        while q:
            d, i, j = heapq.heappop(q)

            if [i, j] == destination:
                return d

            for di, dj in dirs:
                tmp_i, tmp_j, tmp_d = i, j, 0
                while 0 <= tmp_i + di < m and 0 <= tmp_j + dj < n and maze[tmp_i + di][tmp_j + dj] != 1:
                    tmp_i += di
                    tmp_j += dj
                    tmp_d += 1
                
                if (tmp_i, tmp_j) not in stopped or d + tmp_d < stopped[tmp_i, tmp_j]:
                    stopped[tmp_i, tmp_j] = d + tmp_d
                    heapq.heappush(q, (d + tmp_d, tmp_i, tmp_j))
        
        return -1
        