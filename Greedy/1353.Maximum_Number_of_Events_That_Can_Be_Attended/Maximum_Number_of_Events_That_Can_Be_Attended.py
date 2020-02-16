class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # greedy
        events.sort(key=lambda x:x[1])
        vis = set()
        
        for s, e in events:
            while s <= e and s in vis:
                s += 1
            
            if s <= e:
                vis.add(s)
        
        return len(vis)
        