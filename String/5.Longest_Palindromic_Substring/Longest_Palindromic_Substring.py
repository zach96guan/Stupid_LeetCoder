class Solution:
    def longestPalindrome(self, s: str) -> str:
       # Expand from center, O(N^2), O(1)
        ret = ""
        for i in range(len(s)):
            tmp1 = self.helper(s, i, i)
            if len(tmp1) > len(ret):
                ret = tmp1
            tmp2 = self.helper(s, i, i+1)
            if len(tmp2) > len(ret):
                ret = tmp2
        
        return ret
    
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
    