class Solution:
    def deleteTreeNodes(self, nodes: int, parents: List[int], values: List[int]) -> int:
        # dfs
        children = collections.defaultdict(set)
        for i, p in enumerate(parents):
            children[p].add(i)

        def dfs(i):
            value, cnt = values[i], 1
            for child in children[i]:
                next_v, next_cnt = dfs(child)
                value += next_v
                cnt += next_cnt
                
            return value, cnt if value != 0 else 0
        
        return dfs(0)[1]
    