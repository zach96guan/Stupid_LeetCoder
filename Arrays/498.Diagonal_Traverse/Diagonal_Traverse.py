class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        m, n = len(matrix), len(matrix[0])
        ret = []
        dic = collections.defaultdict(list)
    
        for i in range(m):
            for j in range(n):
                dic[i + j + 1].append(matrix[i][j]) # starting indices from 1

        for k in sorted(dic.keys()):
            if k & 1 == 1:
                dic[k].reverse()
            ret.extend(dic[k])
                           
        return ret
        