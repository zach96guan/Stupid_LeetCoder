import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # deque, O(N), O(N)
        ret = []
        q = collections.deque()
        
        for i, num in enumerate(nums):
            while q and nums[q[-1]] < num:
                q.pop()
            q.append(i)
            
            if q[0] + k == i:
                q.popleft()
            
            if i >= k - 1:
                ret.append(nums[q[0]])
        
        return ret
        