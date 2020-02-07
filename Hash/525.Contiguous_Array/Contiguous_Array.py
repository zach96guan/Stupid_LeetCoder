class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # O(N)
        dic = {0: -1}
        cur = ret = 0
        
        for i, num in enumerate(nums):
            if num == 1:
                cur += 1
            else:
                cur -= 1
            
            if cur in dic:
                ret = max(ret, i - dic[cur])
            else:
                dic[cur] = i
        
        return ret
        