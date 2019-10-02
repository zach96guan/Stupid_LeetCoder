class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        g = collections.defaultdict(dict)
        
        for s, d, w in flights:
            g[s][d] = w
        
        ret = {}
        q = [(0, 0, src)]
        while q:
            cost, k, node = heapq.heappop(q)
            if k > K + 1 or cost > ret.get((k, node), float('inf')):
                continue
            
            if node == dst:
                return cost
            
            for next_node in g[node]:
                new_cost = cost + g[node][next_node]
                if new_cost < ret.get((k + 1, next_node), float('inf')):
                    ret[(k + 1, next_node)] = new_cost
                    heapq.heappush(q, (new_cost, k + 1, next_node))
        
        return -1
        