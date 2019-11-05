class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.flag = False  # is end

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for ch in word:
            cur = cur.children[ch]
        cur.flag = True


class StreamChecker:
    # Trie, O(NW), W is maximum length of words
    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.letters = []
        for word in words:
            self.trie.insert(word[::-1])

    def query(self, letter: str) -> bool:
        self.letters.append(letter)
        root = self.trie.root
        
        i = len(self.letters) - 1
        while i >= 0:
            if root.flag:
                return True
            if self.letters[i] not in root.children:
                return False
            
            root = root.children[self.letters[i]]
            i -= 1
            
        return root.flag
        

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)