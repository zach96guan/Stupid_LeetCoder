class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # sliding window, O(N), O(K)
        dic = {}
        ret = l = 0

        for r, ch in enumerate(s):
            if ch in dic and l <= dic[ch]:
                l = dic[ch] + 1
            
            else:
                ret = max(ret, r - l + 1)
            
            dic[ch] = r
        
        return ret
            