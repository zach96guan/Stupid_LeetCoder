class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # stack
        ret = num = 0
        sign = 1
        stack = []
        
        for ch in s:
            if ch.isdigit():
                num = 10 * num + ord(ch) - ord('0')
            
            if ch in "-+":
                ret += sign * num
                sign = 1 if ch == "+" else -1
                num = 0
            
            if ch == "(":
                stack.append(ret)
                stack.append(sign)
                sign = 1
                ret = 0
            
            if ch == ")":
                ret += sign * num
                ret *= stack.pop()
                ret += stack.pop()
                num = 0
        
        return ret + num * sign
        
        