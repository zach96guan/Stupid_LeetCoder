class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # backtrack
        self.board = board
        self.solve()
    
    def find_blank(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '.':
                    return i, j
        return -1, -1
    
    def solve(self):
        i, j = self.find_blank()
        if i == -1 and j == -1:
            return True
        for num in list(map(str, range(1, 10))):
            if self.is_safe(i, j, num):
                self.board[i][j] = num
                if self.solve():
                    return True
                self.board[i][j] = '.'
        return False
    
    def is_safe(self, i, j, num):
        box_i = i - i % 3
        box_j = j - j % 3
        if self.row_safe(i, num) and self.col_safe(j, num) and self.box_safe(box_i, box_j, num):
            return True
        else:
            return False
    
    def row_safe(self, i, num):
        for j in range(9):
            if self.board[i][j] == num:
                return False
        return True
    
    def col_safe(self, j, num):
        for i in range(9):
            if self.board[i][j] == num:
                return False
        return True
    
    def box_safe(self, i, j, num):
        for bi in range(i, i + 3):
            for bj in range(j, j + 3):
                if self.board[bi][bj] == num:
                    return False
        return True  
        