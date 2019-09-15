class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # O(M*N)
        def helper(s):
            return s == s[::-1]
    
        ret = []
        count = {word:i for i, word in enumerate(words)}
        
        for word, i in count.items():
            n = len(word)
            for j in range(n+1):
                prefix = word[:j]
                suffix = word[j:]
                
                if helper(prefix):
                    reversed = suffix[::-1]
                    if reversed != word and reversed in count:  # avoid duplicates
                        ret.append([count[reversed], i])
                
                if j != n and helper(suffix):
                    reversed = prefix[::-1]
                    if reversed in count:
                        ret.append([i, count[reversed]])
        
        return ret
        