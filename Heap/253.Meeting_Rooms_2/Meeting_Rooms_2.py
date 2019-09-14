import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # pq, O(NlogN), O(N)
        intervals.sort(key=lambda x:x[0])
        q = []
        
        for i in intervals:
            if q and q[0] <= i[0]:
                heapq.heapreplace(q, i[-1])
            else:
                heapq.heappush(q, i[-1])
        
        return len(q)
        