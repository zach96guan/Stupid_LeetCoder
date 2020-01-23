class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        idx = {ch:i for i, ch in enumerate(order)}
        
        for w1, w2 in zip(words, words[1:]):
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return False
            
            for c1, c2 in zip(w1, w2):
                if idx[c1] < idx[c2]:
                    break
                if idx[c1] > idx[c2]:
                    return False
        
        return True
