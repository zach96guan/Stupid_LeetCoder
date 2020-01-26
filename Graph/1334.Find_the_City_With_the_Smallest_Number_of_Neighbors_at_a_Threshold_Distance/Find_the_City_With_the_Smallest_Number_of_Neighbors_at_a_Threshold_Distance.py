class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # floyd
        # O(N^3), O(N^2)
        g = [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            g[i][i] = 0
        
        for s, e, w in edges:
            g[s][e] = g[e][s] = w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    g[i][j] = min(g[i][j], g[i][k] + g[k][j])
        
        ret = []
        for i in range(n):
            tmp = sum(1 for j in range(n) if g[i][j] <= distanceThreshold)
            ret.append((i, tmp))
        
        ret.sort(key=lambda x:(x[1], -x[0]))
        
        return ret[0][0]
        
        