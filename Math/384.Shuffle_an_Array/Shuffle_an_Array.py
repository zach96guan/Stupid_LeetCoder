class Solution:
    # Fisher-Yates Algorithm
    # O(N), O(N)

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        ret = self.nums[:]
        for i in range(len(ret) - 1, 0, -1):
            seed = random.randint(0, i)  # low/high both inclusive
            ret[seed], ret[i] = ret[i], ret[seed] 
            
        return ret


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()