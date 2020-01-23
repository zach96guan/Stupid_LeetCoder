class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        met_dot = met_e = met_digit = False
        
        for i, ch in enumerate(s):
            if ch in '+-':
                if i > 0 and s[i - 1] != 'e':
                    return False
            elif ch == '.':
                if met_dot or met_e: 
                    return False
                met_dot = True
            
            elif ch == 'e':
                if met_e or not met_digit:
                    return False
                met_e = True
                met_digit = False
            
            elif ch.isdigit():
                met_digit = True
            else:
                return False
        
        return met_digit
        