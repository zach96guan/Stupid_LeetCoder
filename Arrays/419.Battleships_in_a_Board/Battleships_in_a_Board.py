class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # O(1)
        if not board:
            return board
        
        m, n = len(board), len(board[0])
        ret = 0
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    if i > 0 and board[i - 1][j] == 'X' or j > 0 and board[i][j - 1] == 'X':
                        continue
                    ret += 1
        
        return ret
        