class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # stack, O(N)
        stack = []
        
        # construct a monotone increasing sequence of digits
        for d in num:
            while k and stack and stack[-1] > d:
                stack.pop()
                k -= 1
            stack.append(d)
        
        while k > 0:
            stack.pop()
            k -= 1
        
        return "".join(stack).lstrip('0') or "0"
        