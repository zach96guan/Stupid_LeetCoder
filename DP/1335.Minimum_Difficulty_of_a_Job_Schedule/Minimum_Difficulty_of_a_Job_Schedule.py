from functools import lru_cache

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # dp
        n = len(jobDifficulty)
        
        if n < d:
            return -1

        @lru_cache(None)
        def dfs(i, d):
            if d == 1:
                return max(jobDifficulty[i:])
            
            ret = float('inf')
            max_d = 0
            for j in range(i, n - d + 1):
                max_d = max(max_d, jobDifficulty[j])
                ret = min(ret, max_d + dfs(j + 1, d - 1))
            
            return ret
        
        return dfs(0, d)
        
        