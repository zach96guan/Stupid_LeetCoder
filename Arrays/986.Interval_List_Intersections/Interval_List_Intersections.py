class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        # O(M + N)
        ret = []
        i = j = 0
        
        while i < len(A) and j < len(B):
            l = max(A[i][0], B[j][0])
            r = min(A[i][1], B[j][1])
            
            if l <= r:
                ret.append([l, r])
            
            if A[i][1] <= B[j][1]:
                i += 1
            else:
                j += 1
        
        return ret
        