class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointers
        ret = 0
        l, r = 0, len(height) - 1
        
        while l < r:
            tmp = min(height[l], height[r]) * (r - l)
            ret = max(ret, tmp)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return ret
