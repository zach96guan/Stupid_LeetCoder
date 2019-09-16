class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(nlogn)
        l, r = 1, len(nums)
        
        while l < r:
            m = l + r >> 1
            cnt = 0
            
            for num in nums:
                if num <= m:
                    cnt += 1
            
            if cnt > m:
                r = m
            else:
                l = m + 1
        
        return l

    
        # O(n)
#         fast = slow = nums[0]
#         while True:
#             slow = nums[slow]
#             fast = nums[nums[fast]]
#             if slow == fast:
#                 break
        
#         p = nums[0]
#         q = slow
#         while p != q:
#             p = nums[p]
#             q = nums[q]
#         return p
