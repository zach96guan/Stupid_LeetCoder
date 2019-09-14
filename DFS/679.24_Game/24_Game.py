class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        # dfs, backtrack
        eps = 1e-8
        if len(nums) == 1:
            if abs(nums[0] - 24) <= eps:
                return True
            else:
                return False
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                
                tmp = []
                for k in range(len(nums)):
                    if k not in (i, j):
                        tmp.append(nums[k])
                
                if self.judgePoint24(tmp + [nums[i] + nums[j]]):
                    return True
                if self.judgePoint24(tmp + [nums[i] - nums[j]]):
                    return True
                if self.judgePoint24(tmp + [nums[i] * nums[j]]):
                    return True
                if nums[j] and self.judgePoint24(tmp + [nums[i] / nums[j]]):
                    return True
        return False
