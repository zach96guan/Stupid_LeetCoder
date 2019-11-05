class Solution:
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        # backtrack + greedy
        count = collections.defaultdict(int)
        for x, y, z in transactions:
            count[x] -= z
            count[y] += z
            
        def dfs(balance):
            if not balance:
                return 0
            if not balance[0]:
                return dfs(balance[1:])
            
            for i in range(1, len(balance)):
                if balance[i] + balance[0] == 0:
                    return 1 + dfs(balance[1:i] + balance[i+1:])
            
            ret = float('inf')
            for i in range(1, len(balance)):
                if balance[i] * balance[0] < 0:
                    ret = min(ret, dfs(balance[1:i] + [balance[i] + balance[0]] + balance[i+1:]))
            return ret + 1
    
        return dfs(list(count.values()))
    