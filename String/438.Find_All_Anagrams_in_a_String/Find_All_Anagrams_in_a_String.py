class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # sliding window
        ret = []
        len_p, len_s = len(p), len(s)
        dic_p, dic_s = collections.Counter(p), collections.Counter(s[:len_p - 1])
        
        i = 0
        while i + len_p <= len_s:
            dic_s[s[i + len_p - 1]] += 1
            if dic_s == dic_p:
                ret.append(i)
            dic_s[s[i]] -= 1
            
            if not dic_s[s[i]]:
                del dic_s[s[i]]
            
            i += 1
        
        return ret
        
        