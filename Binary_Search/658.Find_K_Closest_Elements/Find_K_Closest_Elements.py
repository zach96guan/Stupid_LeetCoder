class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # binary search
        n = len(arr)
        l, r = 0, n - k

        while l < r:
            m = l + r >> 1
            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else:
                r = m
                
        return arr[l:l + k]
        