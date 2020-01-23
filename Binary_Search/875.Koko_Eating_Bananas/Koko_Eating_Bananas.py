class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # binary search
        l, r = 1, max(piles)
        
        while l < r:
            m = l + r >> 1
            if sum(math.ceil(p / m) for p in piles) > H:
                l = m + 1
            else:
                r = m
        
        return l   
        