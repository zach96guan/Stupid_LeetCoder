class TrieNode:
    def __init__(self):
        self.word = None
        self.children = collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for char in word:
            root = root.children[char]
        root.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Trie + DFS
        res = []
        if not board:
            return res

        tree = Trie()
        for word in words:
            tree.insert(word)

        for i, row in enumerate(board):
            for j, char in enumerate(row):
                self.dfs(i, j, tree.root, board, res)
        return res
    
    def dfs(self, i, j, root, board, res):
        char = board[i][j]
        if not (char and char in root.children):
            return

        root = root.children[char]
        if root.word:
            res.append(root.word)
            root.word = None
        
        board[i][j] = None
        for dx, dy in ((0, -1), (-1, 0), (0, 1), (1, 0)):
            x, y = i + dx, j + dy
            if 0 <= x < len(board) and 0 <= y < len(board[0]):
                self.dfs(x, y, root, board, res)
        board[i][j] = char
      