class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n^2), O(n)
#         if not nums or not len(nums):
#             return 0
#        
#         dp = [0] * len(nums)
#         dp[0] = 1
#         for i in range(len(nums)):
#             tmp = 0
#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     tmp = max(tmp, dp[j])
#             dp[i] = tmp + 1
#         return max(dp)
        
    
        # follow-up: largest subsequence
        # if not nums or not len(nums):
        #     return 0
        #
        # dp = [0] * len(nums)
        # f = [0] * len(nums)
        # f[0] = nums[0]
        # dp[0] = 1
        # for i in range(1, len(nums)):
        #     dp[i] = 1
        #     f[i] = nums[i]
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             if dp[j] + 1 >= dp[i]:
        #                 dp[i] = max(dp[i], dp[j]+1) 
        #                 f[i] = max(f[i], f[j] + nums[i])
        #             else: 
        #                 f[i] = f[j] + nums[i]
        #
        # ret = max(dp)
        # s = f[0]
        # for i in range(len(nums)):
        #     if dp[i] == ret:
        #         s = max(s, f[i])
        # print(s)
        # return max(dp)
                    

        # O(nlogn), O(n)
        # dp[i]
        # minimal ending of longest increasing subsequence with length i
        if not nums or len(nums) == 0:
            return 0
        
        dp = [0] * len(nums)
        res = 0
        
        for num in nums:
            l, r = 0, res
            while l < r:
                m = l + r >> 1
                if dp[m] < num:
                    l = m + 1
                else:
                    r = m
                    
            dp[l] = num
            res = max(res, l + 1)
            
        return res
