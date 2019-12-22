class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        # bfs
        q = initialBoxes
        cur_keys = set(q)
        vis = set()
        
        while q:
            for _ in range(len(q)):
                cur = q.pop(0)
                for nxt in containedBoxes[cur]:
                    if nxt not in vis:
                        q.append(nxt)
                
                cur_keys |= set(keys[cur])
                vis.add(cur)
        
        return sum(candies[x] for x in vis if status[x] or x in cur_keys)
        
        