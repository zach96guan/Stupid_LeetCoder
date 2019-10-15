class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # topo-
        unique = set("".join(words))
        from_dict = collections.defaultdict(set)
        to_dict = collections.defaultdict(set)
        
        for pair in zip(words, words[1:]):
            for char1, char2 in zip(*pair):
                if char1 != char2:
                    from_dict[char2].add(char1)
                    to_dict[char1].add(char2)
                    break
        
        q = unique - set(from_dict.keys())
        ret = ""
        
        while q:
            char = q.pop()
            ret += char
            for next_char in to_dict[char]:
                from_dict[next_char].discard(char)
                if not from_dict[next_char]:
                    q.add(next_char)
        
        return ret if len(ret) == len(unique) else ""
        