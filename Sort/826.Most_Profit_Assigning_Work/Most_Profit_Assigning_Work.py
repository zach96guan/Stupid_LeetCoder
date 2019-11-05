class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        # sort + two pointers
        # O(NlogN), O(N)
        job = sorted((d, p) for d, p in zip(difficulty, profit))
        i = cur = ret = 0
        
        for ability in sorted(worker):
            while i < len(job) and ability >= job[i][0]:
                cur = max(cur, job[i][1])
                i += 1
                
            ret += cur
            
        return ret
    