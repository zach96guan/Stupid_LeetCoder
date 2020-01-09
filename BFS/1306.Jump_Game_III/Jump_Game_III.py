class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        vis = [-1] * len(arr)
        q = [start]
        
        while q:
            cur = q.pop(0)
            d = arr[cur]
            
            if d == 0:
                return True
            
            vis[cur] = 0
            if cur - d >= 0 and vis[cur - d] == -1:
                q.append(cur - d)
            if cur + d < len(arr) and vis[cur + d] == -1:
                q.append(cur + d)
        
        return False
        