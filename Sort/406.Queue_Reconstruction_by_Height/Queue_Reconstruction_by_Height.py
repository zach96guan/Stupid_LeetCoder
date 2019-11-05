class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # O(N^2), O(N)
        ret = []
        people.sort(key = lambda x:(-x[0], x[1]))
        
        for p in people:
            ret.insert(p[1], p)
            
        return ret
    