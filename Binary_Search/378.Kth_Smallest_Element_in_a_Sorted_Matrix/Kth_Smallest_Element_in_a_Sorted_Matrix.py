class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # binary search
        # O(NlogM), 2N passes, M is the max distance possible, (max_num - min_num).
        # O(1)
        def helper(num):
            ret = 0
            col = 0
            for row in matrix[::-1]:
                while col < len(matrix[0]) and row[col] <= num:
                    col += 1
                ret += col
            return ret
        
        l, r = matrix[0][0], matrix[-1][-1]
        while l < r:
            m = l + r >> 1
            if helper(m) < k:
                l = m + 1
            else:
                r = m
        return l
        