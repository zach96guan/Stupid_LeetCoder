class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        # sliding window
        dic = collections.Counter()
        l = r = 0
        
        while r < len(s):
            dic[s[r]] += 1
            r += 1
            
            if len(dic) > 2:
                dic[s[l]] -= 1
                if not dic[s[l]]:
                    del dic[s[l]]
                l += 1
        
        return r - l
        