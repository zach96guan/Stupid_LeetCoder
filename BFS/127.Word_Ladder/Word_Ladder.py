class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # bfs, O(M*N), O(M*N)
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0
        
        n = len(beginWord)
        all_combo = collections.defaultdict(list)
        
        for word in wordList:
            for i in range(n):
                tmp = word[:i] + '*' + word[i+1:]
                all_combo[tmp].append(word)
        
        q = [(beginWord, 1)]
        vis = set(beginWord)
        
        while q:
            curWord, t = q.pop(0)
            for i in range(n):
                tmp = curWord[:i] + '*' + curWord[i+1:]
                for nextWord in all_combo[tmp]:
                    if nextWord in vis:
                        continue
                    if nextWord == endWord:
                        return t + 1
                    vis.add(nextWord)
                    q.append((nextWord, t + 1))
                    
        return 0        
    