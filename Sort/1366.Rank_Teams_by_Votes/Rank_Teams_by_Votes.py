class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        dic = collections.defaultdict(lambda: [0] * 26)

        for vote in votes:
            for rank, char in enumerate(vote):
                dic[char][rank] -= 1
        
        ret = sorted(dic.items(), key=lambda x: (x[1], x[0]))
        return "".join(k for k, v in ret)
