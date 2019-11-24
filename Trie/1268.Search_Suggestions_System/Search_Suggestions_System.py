class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_list = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for char in word:
            cur = cur.children[char]
            cur.word_list.append(word)
            
            cur.word_list.sort()
            while len(cur.word_list) > 3:
                cur.word_list.pop()
    
    def search(self, word):
        find = []
        cur = self.root
        
        for char in word:
            if char not in cur.children:
                break
            cur = cur.children[char]
            find.append(cur.word_list)
        
        find += [[] for _ in range(len(word) - len(find))]
        
        return find

    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Trie
        trie = Trie()
        for p in products:
            trie.insert(p)
        
        return trie.search(searchWord)
    
    