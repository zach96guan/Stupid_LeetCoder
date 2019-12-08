class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)

        while l < r:
            m = l + r >> 1
            # print(l, m, r)

            tmp = 0
            for num in nums:
                tmp += math.ceil(num / m)

            if tmp > threshold:
                l = m + 1
            else:
                r = m

        return l
