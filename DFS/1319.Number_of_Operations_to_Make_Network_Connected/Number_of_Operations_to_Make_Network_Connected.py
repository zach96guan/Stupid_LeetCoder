from collections import defaultdict

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        g = defaultdict(set)
        for i, j in connections:
            g[i].add(j)
            g[j].add(i)
        
        cnt = 0
        vis = set()
        
        def dfs(cur):
            if cur not in vis:
                vis.add(cur)
                for nxt in g[cur]:
                    dfs(nxt)
        
        for cur in g:
            if cur not in vis:
                dfs(cur)
                cnt += 1
        
        return cnt + (n - len(vis)) - 1
        
        