class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topo
        # O(N), O(N)
        g = [[] for _ in range(numCourses)]
        degree = [0] * numCourses
        
        for a, b in prerequisites:
            g[b].append(a)
            degree[a] += 1
        
        ret = []
        for i, d in enumerate(degree):
            if d == 0:
                ret.append(i)
        
        pos = 0
        while len(ret) > pos:
            x = ret[pos]
            pos += 1
            
            for nx in g[x]:
                degree[nx] -= 1
                if degree[nx] == 0:
                    ret.append(nx)
        
        return ret if len(ret) == numCourses else []
                