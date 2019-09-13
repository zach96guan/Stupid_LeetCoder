class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # one-pass, O(1), O(1)
        if not board or len(board) == 0:
            return False
        
        for i in range(9):
            rows, cols, blocks = set(), set(), set()
            
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in rows:
                        return False
                    else:
                        rows.add(board[i][j])
                
                if board[j][i] != '.':
                    if board[j][i] in cols:
                        return False;
                    else:
                        cols.add(board[j][i])
                
                rowId, colId = 3 * (i // 3), 3 * (i % 3)
                tmp = board[rowId + j // 3][colId + j % 3]
                if tmp != '.':
                    if tmp in blocks:
                        return False
                    else:
                        blocks.add(tmp)
        
        return True
        