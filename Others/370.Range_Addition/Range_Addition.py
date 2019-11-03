class Solution:
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        # range caching, O(N + K), O(1)
        ret = [0] * (length + 1)
        
        for s, e, inc in updates:
            ret[s] += inc
            ret[e + 1] -= inc
        
        for i in range(1, len(ret)):
            ret[i] += ret[i - 1]
        
        return ret[:-1]
    