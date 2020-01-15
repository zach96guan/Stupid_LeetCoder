class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int: 
        # O(N), O(N)
        pre = ret = 0
        dic = collections.defaultdict(int)
        dic[0] = 1
        
        for num in nums:
            pre += num
            ret += dic[pre - k]
            dic[pre] += 1
        
        return ret
        