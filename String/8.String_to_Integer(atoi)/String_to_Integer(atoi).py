class Solution:
    def myAtoi(self, s: str) -> int:
        # INT_MAX (2^31 − 1) or INT_MIN (−2^31) 
        s = s.strip()
        ret = 0
        
        if not s or len(s) == 0:
            return ret
        
        flag = None
        if s[0] in '+-':
            flag = 1 if s[0] == '+' else -1
        
        pos = 1 if flag else 0
        while pos < len(s) and s[pos].isdigit():
            ret = 10 * ret + int(s[pos])
            pos += 1
        
        ret = flag * ret if flag else ret
        ret = max(min(2**31 - 1, ret), -2**31)
        
        return ret
        