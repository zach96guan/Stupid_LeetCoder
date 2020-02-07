class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointers
        l, r = 0, len(height) - 1
        ret = cur = 0
        
        while l < r:
            while l < r and cur >= height[l]:
                ret += cur - height[l]
                l += 1
            
            while l < r and cur >= height[r]:
                ret += cur - height[r]
                r -= 1
            
            cur = min(height[l], height[r])
            
        return ret
    