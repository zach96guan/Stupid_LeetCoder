class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = [p for p in path.split('/') if p and p != '.']
        stack = []
        
        for p in paths:
            if p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        
        return '/' + '/'.join(stack)
        