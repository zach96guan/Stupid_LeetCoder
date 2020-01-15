class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # O(N), O(min(N, k))
        pre = 0
        dic = collections.defaultdict(int)
        dic[0] = -1
        
        for i, num in enumerate(nums):
            pre += num
            if k != 0:
                pre %= k
            
            if pre in dic:
                if i - dic[pre] >= 2:
                    return True
            else:
                dic[pre] = i
        
        return False
        