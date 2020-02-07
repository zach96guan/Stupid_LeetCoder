class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # dfs, from boundary 'O'
        if not board:
            return
        
        m, n = len(board), len(board[0])
        
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != 'O':
                return
            board[r][c] = '*'
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
            
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m-1 or j == 0 or j == n-1) and board[i][j] == 'O':
                    dfs(i, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == '*':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
            