class Solution:
    def lastSubstring(self, s: str) -> str:
        # two pointers, O(N), O(1)
        n = len(s)
        i, j, k = 0, 1, 0
        
        while j + k < n:
            if s[i + k] == s[j + k]:
                k += 1
                continue
            elif s[i + k] > s[j + k]:
                j += k + 1
            else:
                i += k + 1
                j = i + 1
            k = 0
        
        return s[i:]
        