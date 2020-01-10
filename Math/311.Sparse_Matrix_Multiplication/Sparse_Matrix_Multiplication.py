from collections import defaultdict

class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        # use two tables, more efficient
        m, n, p = len(A), len(A[0]), len(B[0])
        table_A, table_B = defaultdict(dict), defaultdict(dict)
        
        for i, row in enumerate(A):
            for j, num_A in enumerate(row):
                if num_A:
                    table_A[i][j] = num_A
        
        for i, row in enumerate(B):
            for j, num_B in enumerate(row):
                if num_B:
                    table_B[i][j] = num_B
                            
        AB = [[0] * p for _ in range(m)]
        for i in table_A:
            for k in table_A[i]:
                if k in table_B:
                    for j in table_B[k]:
                        AB[i][j] += table_A[i][k] * table_B[k][j]
        
        return AB
        