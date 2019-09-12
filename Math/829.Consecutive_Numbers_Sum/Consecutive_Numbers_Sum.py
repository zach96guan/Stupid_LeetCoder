class Solution:
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        # mathematical, O(sqrt(N)), O(1)
        # N = x +...+ (x+k-1), k items
        # no need to calculate x, N = kx + k(k-1)/2, k >= 2 and k(k-1)/2 < N
             
        res = 1  # N itself
        for k in range(2, math.ceil((2*N) ** 0.5)):
            if (N - k * (k - 1) // 2) % k == 0:
                res += 1
        return res
    