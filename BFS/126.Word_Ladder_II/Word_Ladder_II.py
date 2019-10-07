class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # bfs + dfs
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return []
        
        all_combo = collections.defaultdict(list)
        n = len(beginWord)
        
        for word in wordList:
            for i in range(n):
                tmp = word[:i] + '*' + word[i+1:]
                all_combo[tmp].append(word)
        
        q = [beginWord]
        vis = set(beginWord)
        pre = collections.defaultdict(set)  # record path
        
        while q:
            flag = False
            pre_set = vis.copy()
            for _ in range(len(q)):
                curWord = q.pop(0)
                for i in range(n):
                    tmp = curWord[:i] + '*' + curWord[i+1:]
                    for nextWord in all_combo[tmp]:
                        if nextWord == curWord:  # avoid cycle
                            continue
                        
                        if nextWord == endWord:
                            flag = True
                        if nextWord not in vis:
                            vis.add(nextWord)                            
                            q.append(nextWord)
                            
                        if nextWord not in pre_set:
                            pre[nextWord].add(curWord)
                    
                    all_combo[curWord] = []
            if flag:
                break
        
        ret = []
        def dfs(cur, path, vis):
            vis.add(cur)
            if cur == beginWord:
                path.append(cur)
                ret.append(path[::-1])
                path.pop()
                vis.remove(cur)
                return
            for next_w in pre[cur]:
                if next_w in vis:
                    continue
                path.append(cur)
                dfs(next_w, path, vis)
                path.pop()
            vis.remove(cur)
                
        dfs(endWord, [], set()) 
        return ret
    