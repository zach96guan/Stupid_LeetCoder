class Solution:
    def minimumDistance(self, word: str) -> int:
        def pos(ch):
            d = ord(ch) - ord('A')
            return d // 6, d % 6

        def dist(pair):
            (x1, y1), (x2, y2) = pos(pair[0]), pos(pair[1])
            return abs(x1 - x2) + abs(y1 - y2)
        
        n = len(word)
        dp = {(0, -1) : 0}
        # key: (i, k), i, k are the positions of the first/second finger (-1 means "free")
        # base case: when there's only 1 character to type, we only use one finger with 0 distance
        
        for i in range(1, n):
            dp2 = collections.defaultdict(lambda:float('inf'))
            for (f1, f2), d in dp.items():
                dp2[f1 + 1, f2] = min(dp2[f1 + 1, f2], dist(word[i - 1:i + 1]) + d)

                if f2 > -1:
                    dp2[f1 + 1, f1] = min(dp2[f1 + 1, f1], dist(word[f2] + word[f1 + 1]) + d)

                else:
                    dp2[f1 + 1, f1] = min(dp2[f1 + 1, f1], d)

            dp = dp2                    

        return min(dp.values())
    