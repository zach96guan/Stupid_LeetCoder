class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10 ** 9 + 7
        return (math.factorial(2 * n) >> n) % mod
        