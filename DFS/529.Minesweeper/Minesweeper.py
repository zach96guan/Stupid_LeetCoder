class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # dfs
        if not board:
            return []

        m, n = len(board), len(board[0])
        i, j = click[0], click[1]

        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board

        self.dfs(board, i, j)
        return board
    
    
    def dfs(self, board, i, j):
        m, n = len(board), len(board[0])
        
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'E':
            return

        dirs = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
        cnt = 0

        for d in dirs:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'M':        
                cnt += 1

        if cnt > 0:
            board[i][j] = str(cnt)
            return
        
        board[i][j] = 'B'
        for d in dirs:
            ni, nj = i + d[0], j + d[1]
            self.dfs(board, ni, nj)
        
        