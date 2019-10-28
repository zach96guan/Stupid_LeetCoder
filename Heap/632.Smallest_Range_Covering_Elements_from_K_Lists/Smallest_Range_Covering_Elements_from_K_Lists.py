class Solution:
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        # heap, O(nlogk), O(k)
        q = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(q)
        
        # min-max
        ret = [float('-inf'), float('inf')]
        r = max(row[0] for row in nums)
        
        while q:
            l, i, j = heapq.heappop(q)
            
            if r - l < ret[1] - ret[0]:
                ret = [l, r]
            if j == len(nums[i]) - 1:
                return ret
            
            tmp = nums[i][j + 1]
            r = max(r, tmp)
            heapq.heappush(q, (tmp, i, j + 1))