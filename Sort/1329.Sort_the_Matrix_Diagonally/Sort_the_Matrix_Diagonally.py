class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dic = collections.defaultdict(list)
        
        for i in range(m):
            for j in range(n):
                dic[i - j].append(mat[i][j])
        
        for k in dic:
            dic[k].sort()
            
        for i in range(m):
            for j in range(n):
                mat[i][j] = dic[i - j].pop(0)
        
        return mat
        