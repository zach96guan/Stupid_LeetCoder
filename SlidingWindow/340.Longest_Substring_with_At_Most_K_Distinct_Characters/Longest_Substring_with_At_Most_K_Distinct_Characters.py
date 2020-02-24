class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # sliding window
        dic = {}
        ret = l = 0
        
        for r, ch in enumerate(s):
            dic[ch] = r
            
            if len(dic) > k:
                leftmost = min(dic.values())
                del dic[s[leftmost]]
                l = leftmost + 1
            
            ret = max(ret, r - l + 1)
        
        return ret
                
        