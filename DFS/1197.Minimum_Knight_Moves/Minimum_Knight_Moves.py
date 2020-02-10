class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # dfs + memo
        memo = {(0, 0): 0, (1, 0): 3, (0, 1): 3, (1, 1): 2}
        
        def dfs(x, y):
            if (x, y) in memo:
                return memo[x, y]
            
            ret = min(dfs(abs(x - 1), abs(y - 2)), dfs(abs(x - 2), abs(y - 1))) + 1
            memo[x, y] = ret
            return ret
        
        return dfs(abs(x), abs(y))
        