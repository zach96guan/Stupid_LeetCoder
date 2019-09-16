class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # stack, O(N), O(N)
        stack = []
        digits = chars = ""
        
        for i, ch in enumerate(s):
            if ch.isdigit():
                digits += ch
            elif ch == '[':
                stack.append((digits, chars))
                digits = chars = ""
            elif ch == ']':
                pre_digits, pre_chars = stack.pop()
                chars = pre_chars + int(pre_digits) * chars
            else:
                chars += ch
        
        return chars
    