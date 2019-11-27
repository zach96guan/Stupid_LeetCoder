class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        # binary search
        n = len(arr)
        d = (arr[-1] - arr[0]) // n
        
        l, r = 0, n - 1
        while l < r:
            m = l + r >> 1
            if arr[m] == arr[0] + d * m:
                l = m + 1
            else:
                r = m
                
        return arr[0] + d * l
    