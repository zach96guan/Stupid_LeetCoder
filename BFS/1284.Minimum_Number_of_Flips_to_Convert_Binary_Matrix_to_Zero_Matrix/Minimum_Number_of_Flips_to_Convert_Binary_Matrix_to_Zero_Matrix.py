class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        # bfs
        m, n = len(mat), len(mat[0])
        
        def to_tuple(mat):
            return tuple(tuple(r) for r in mat)
        
        def to_list(tuple_mat):
            return [list(r) for r in tuple_mat]
        
        def all_zero(mat):
            return all(x == 0 for r in mat for x in r)
        
        def flip(mat, i, j):
            mat[i][j] ^= 1
            if i > 0: mat[i - 1][j] ^= 1
            if i < m - 1: mat[i + 1][j] ^= 1
            if j > 0: mat[i][j - 1] ^= 1
            if j < n - 1: mat[i][j + 1] ^= 1
      
        q = [(to_tuple(mat), 0)]
        vis = set()
        
        while q:
            tuple_mat, step = q.pop(0)
            if all_zero(to_list(tuple_mat)):
                return step
            if tuple_mat in vis:
                continue
            
            vis.add(tuple_mat)
            mat = to_list(tuple_mat)
            for i in range(m):
                for j in range(n):
                    flip(mat, i, j)
                    q.append((to_tuple(mat), step + 1))
                    flip(mat, i, j)

        return -1
    
    