class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # O(2^N)
        self.ret = []
        self.backtrack(candidates, target, 0, [])
        return self.ret
    
    
    def backtrack(self, nums, target, pos, tmp):
        if target == 0:
            self.ret.append(tmp)
            return
        
        if pos == len(nums) or target < 0:
            return
        
        for i in range(pos, len(nums)):
            self.backtrack(nums, target - nums[i], i, tmp + [nums[i]])
        