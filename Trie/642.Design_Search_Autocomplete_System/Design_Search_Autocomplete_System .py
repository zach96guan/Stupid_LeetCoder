class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.flag = False
        self.words = ""
        self.rank = 0

        
class AutocompleteSystem:
    # Trie, O(K*N)
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.key = ""
        for i, sent in enumerate(sentences):
            self.insert(sent, times[i])
    
    
    def insert(self, sent, count):
        cur = self.root
        for ch in sent:
            cur = cur.children[ch]
        cur.flag = True
        cur.words = sent
        cur.rank -= count
    
    
    def dfs(self, root):
        ret = []
        if root:
            if root.flag:
                ret.append((root.rank, root.words))
            for child in root.children:
                ret.extend(self.dfs(root.children[child]))
        return ret
    
    
    def search(self, sent):
        cur = self.root
        for ch in sent:
            if ch not in cur.children:
                return []
            cur = cur.children[ch]
        return self.dfs(cur)
    
    
    def input(self, c: str) -> List[str]:
        ret = []
        if c != "#":
            self.key += c
            ret = self.search(self.key)
        else:
            self.insert(self.key, 1)
            self.key = ""
        
        return [x[1] for x in sorted(ret)[:3]]



# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)