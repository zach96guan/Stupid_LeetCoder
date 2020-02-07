class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # two pointers
#         ns, nt = len(s), len(t)
        
#         if not ns:
#             return True
        
#         if not nt:
#             return False
        
#         i, j = 0, 0
#         while i < ns and j < nt:
#             if s[i] == t[j]:
#                 i += 1
#             j += 1
            
#         return i == ns
    
        # follow-up
        idx = collections.defaultdict(list)
        for i, ch in enumerate(t):
            idx[ch].append(i)
        
        pos = 0
        for i, ch in enumerate(s):            
            j = bisect.bisect_left(idx[ch], pos)
            if j == len(idx[ch]): 
                return False
            
            pos = idx[ch][j] + 1
        
        return True
    
    