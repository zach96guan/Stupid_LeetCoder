class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # deque, time: O(N), space: O(N), O(k)
        ret = []
        q = collections.deque()  # record index
        
        for i, num in enumerate(nums):
            if q and i == q[0] + k:
                q.popleft()
            
            # remove indices of smaller elements
            while q and num > nums[q[-1]]:
                q.pop()
            q.append(i)

            if i >= k - 1:
                ret.append(nums[q[0]])
        return ret