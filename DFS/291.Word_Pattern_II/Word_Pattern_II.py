class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        # dfs, backtrack
        return self.dfs(pattern, s, {})
    
    def dfs(self, pattern, s, dic):
        if not (pattern or s):
            return True
        if not (pattern and s):
            return False
        
        for end in range(1, len(s) - len(pattern) + 2):
            word = pattern[0]
            if word not in dic and s[:end] not in dic.values():
                dic[word] = s[:end]
                if self.dfs(pattern[1:], s[end:], dic):
                    return True
                del dic[word]
            
            elif word in dic and dic[word] == s[:end]:
                if self.dfs(pattern[1:], s[end:], dic):
                    return True
                
        return False
    