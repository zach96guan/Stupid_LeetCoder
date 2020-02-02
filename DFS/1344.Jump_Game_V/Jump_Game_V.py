class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        # dfs
        n = len(arr)
        g = collections.defaultdict(set)
        
        for i in range(n):
            for x in range(1, d + 1):
                if i - x >= 0 and arr[i - x] < arr[i]:
                    g[i].add(i - x)
                else:
                    break
            
            for x in range(1, d + 1):
                if i + x < n and arr[i + x] < arr[i]:
                    g[i].add(i + x)
                else:
                    break
        
        memo = collections.defaultdict(lambda: 1)
        def dfs(v):
            if memo[v] != 1:
                return memo[v]
            for nxt in g[v]:
                memo[v] = max(memo[v], 1 + dfs(nxt))
            return memo[v]
        
        ret = 1
        for k in range(n):
            ret = max(ret, dfs(k))
        return ret
        
        