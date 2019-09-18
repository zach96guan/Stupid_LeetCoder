class Solution:
    def myPow(self, x: float, n: int) -> float:
        # iterative, O(logN), O(1)
        if n < 0:
            x = 1 / x
            n = -n
        
        ret = 1.0
        while n >= 1:
            if n & 1 == 1:
                n -= 1
                ret *= x
            else:
                n //= 2
                x **= 2
        
        return ret
        