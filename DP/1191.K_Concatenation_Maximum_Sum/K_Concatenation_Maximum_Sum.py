class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        if not arr or k < 1:
            return 0
        
        cur, ret = 0, float('-inf')
        n = len(arr)
        mod = 10**9 + 7
        
        for i in range(n * min(k, 2)):
            cur += arr[i % n]
            cur = max(cur, 0)
            ret = max(ret, cur)
        
        if k > 2:
            ret += max((k-2) * sum(arr), 0)  # only repeat twice
        
        return 0 if ret < 0 else ret % mod
        