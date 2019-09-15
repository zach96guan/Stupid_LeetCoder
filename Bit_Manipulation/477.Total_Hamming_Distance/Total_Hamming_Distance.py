class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        # bit manipulate
        # O(N), O(1)
        ret = 0
        n = len(nums)
        
        for i in range(32):
            tmp = 0
            for j, num in enumerate(nums):
                tmp += (num >> i) & 1
            
            # between pairs
            ret += tmp * (n - tmp)
        
        return ret
        