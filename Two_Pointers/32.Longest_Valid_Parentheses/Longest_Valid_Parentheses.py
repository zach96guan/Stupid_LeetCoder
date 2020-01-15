class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # using stack
        # O(N)
        # ret = 0
        # stack = [-1]

        # for i, ch in enumerate(s):
        #    if ch == ")":
        #        stack.pop()
        #        if stack:
        #            ret = max(ret, i - stack[-1])
        #            continue
                    
        #    stack.append(i)
            
        # return ret
        
        # two pointers
        # O(N), O(1)
        ret = l = r = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            
            if l == r:
                ret = max(ret, l * 2)
            elif r > l:
                l = r = 0
        
        l = r = 0
        for j in range(len(s) - 1, -1, -1):
            if s[j] == '(':
                l += 1
            else:
                r += 1
            
            if l == r:
                ret = max(ret, l * 2)
            elif l > r:
                l = r = 0
        
        return ret
        
        