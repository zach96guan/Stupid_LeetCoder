class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # pq, O(N), O(1)
        ret = 0
        q = []
        for k, v in collections.Counter(tasks).items():
            heapq.heappush(q, (-v, k))
        
        while q:
            cnt = 0
            tmp = []
            
            while cnt <= n:
                cnt += 1
                ret += 1
                
                if q:
                    v, k = heapq.heappop(q)
                    if v != -1:
                        tmp.append((v+1, k))  # -(-v-1)
                
                if not tmp and not q:
                    break
            
            for item in tmp:
                heapq.heappush(q, item)
            
        return ret
    