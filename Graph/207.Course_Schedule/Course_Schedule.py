class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topo-sort
        g = [[] for _ in range(numCourses)]
        degree = [0] * numCourses
        
        for a, b in prerequisites:
            g[b].append(a)
            degree[a] += 1
        
        q = []
        for i, d in enumerate(degree):
            if d == 0:
                q.append(i)
        
        for x in q:
            for nx in g[x]:
                degree[nx] -= 1
                if degree[nx] == 0:
                    q.append(nx)
                    
        return len(q) == numCourses
        