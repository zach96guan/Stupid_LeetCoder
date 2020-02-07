class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.pre = [0] * (n + 1)
        
        for i in range(1, n + 1):
            self.pre[i] = nums[i - 1] + self.pre[i - 1]
            

    def sumRange(self, i: int, j: int) -> int:
        return self.pre[j + 1] - self.pre[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)