class Solution:
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # sliding window, O(N)
        dq = []
        n = len(A)
        ret = float('inf')
        
        # presum
        for i in range(1, n):
            A[i] += A[i - 1]
        A.insert(0, 0)
        
        for i, a in enumerate(A):
            # mono-increasing
            while dq and a <= A[dq[-1]]:
                dq.pop()
            # update
            while dq and a - A[dq[0]] >= K:
                ret = min(ret, i - dq.pop(0))
            
            dq.append(i)
        
        return ret if ret < float('inf') else -1
        