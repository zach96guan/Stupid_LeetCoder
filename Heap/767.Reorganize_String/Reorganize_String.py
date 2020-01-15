class Solution:
    def reorganizeString(self, S: str) -> str:
        # pq, O(NlogK), O(K)
        pq = [(-v, k) for k, v in collections.Counter(S).items()]
        heapq.heapify(pq)
        
        if -pq[0][0] > (len(S) + 1) // 2:
            return ""

        ret = []
        while len(pq) >= 2:
            v1, k1 = heapq.heappop(pq)
            v2, k2 = heapq.heappop(pq)
            
            ret += [k1, k2]

            if v1 < -1:
                heapq.heappush(pq, (v1 + 1, k1))
            if v2 < -1:
                heapq.heappush(pq, (v2 + 1, k2))

        return "".join(ret) + (pq[0][1] if pq else '')
    