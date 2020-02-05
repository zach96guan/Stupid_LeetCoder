class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack with ascending height
        heights.append(0)
        stack = [-1]
        ret = 0
        
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ret = max(ret, h * w)
            
            stack.append(i)
        
        heights.pop()
        return ret
        