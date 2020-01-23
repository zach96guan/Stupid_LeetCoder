class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # dfs
        self.ret = []
        self.dfs(s, self.invalid(s), {s})
        return self.ret
        
    
    def dfs(self, s, cnt, vis):
        if not cnt:
            self.ret.append(s)
            return
        
        for i, ch in enumerate(s):
            if ch in '()':
                cur = s[:i] + s[i + 1:]
                if cur not in vis and self.invalid(cur) < cnt:  # remove min number
                    vis.add(cur)
                    self.dfs(cur, self.invalid(cur), vis)
            
        
    def invalid(self, s):
        l = r = 0    
        for ch in s:
            if ch == '(':
                l += 1
            if ch == ')':
                l -= 1

            r += 1 if l < 0 else 0
            l = max(0, l)
                
        return l + r

    