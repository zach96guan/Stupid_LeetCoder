class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(N), O(N)
        h = set(nums)
        ret = 0
        
        for num in h:
            if num - 1 not in h:
                cnt = 1
                while num + 1 in h:
                    num += 1
                    cnt += 1
                
                ret = max(ret, cnt)
        
        return ret
        