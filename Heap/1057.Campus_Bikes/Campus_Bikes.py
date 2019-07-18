class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        q = []
        for i, w in enumerate(workers):
            for j, b in enumerate(bikes):
                d = abs(w[0] - b[0]) + abs(w[-1] - b[-1])
                q.append((d, i, j))
        q.sort()
        
        s = set() # assigned bike
        res = [-1] * len(workers) 
        for _, w_id, b_id in q:
            if len(s) == len(workers):
                    break
            if b_id not in s and res[w_id] == -1:
                s.add(b_id)
                res[w_id] = b_id
        return res