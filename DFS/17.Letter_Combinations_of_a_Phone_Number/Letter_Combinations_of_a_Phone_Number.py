class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # backtrack
        dic = {
            '2': ['a', 'b', 'c'], 
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        if not digits:
            return []
        
        ret = []
        def backtrack(comb, remain):
            if len(remain) == 0:
                ret.append(comb)
                return
            for char in dic[remain[0]]:
                backtrack(comb + char, remain[1:])
        
        backtrack("", digits)
        return ret
    