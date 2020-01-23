class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # O(N)
        f = [float('-inf')] * 3
        
        for num in nums:
            if num not in f:
                if num > f[0]:
                    f = [num, f[0], f[1]]
                elif num > f[1]:
                    f = [f[0], num, f[1]]
                elif num > f[2]:
                    f = [f[0], f[1], num]
                    
        return max(nums) if float('-inf') in f else f[-1]
        