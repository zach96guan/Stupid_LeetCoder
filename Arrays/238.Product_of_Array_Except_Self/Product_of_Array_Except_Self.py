class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [1] * n
        
        i, j = 0, n - 1
        l = r = 1
        
        while i <= n - 2 and j >= 1:
            l *= nums[i]
            r *= nums[j]
            
            ret[i + 1] *= l
            ret[j - 1] *= r
            i += 1
            j -= 1

        return ret