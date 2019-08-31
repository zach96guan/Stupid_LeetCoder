class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # O(N), O(N), one pass
        ret = score = 0
        map = {}
        
        for i, h in enumerate(hours):
            score = score + 1 if h > 8 else score - 1
            
            if score > 0:
                ret = i + 1
            map.setdefault(score, i)
            
            if score - 1 in map:
                ret = max(ret, i - map[score - 1])
        
        return ret
