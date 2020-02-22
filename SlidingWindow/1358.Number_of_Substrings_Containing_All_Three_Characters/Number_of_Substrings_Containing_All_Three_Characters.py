class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # sliding window
        pre = {}
        pre[0] = pre[1] = pre[2] = -1
        ret = 0
        
        for i, ch in enumerate(s):
            pre[ord(ch) - ord('a')] = i
            ret += 1 + min(pre.values())
        
        return ret
        