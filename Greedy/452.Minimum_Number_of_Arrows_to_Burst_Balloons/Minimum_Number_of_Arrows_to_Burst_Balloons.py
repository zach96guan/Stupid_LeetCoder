class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # greedy
        if not points:
            return 0
        
        points.sort(key=lambda x:x[1])
        
        ret = 1
        cur = points[0][1]
        
        for s, e in points[1:]:
            if s > cur:
                ret += 1
                cur = e
        
        return ret
        
        