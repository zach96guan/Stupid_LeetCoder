class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # dfs
        dic = collections.defaultdict(list)
        for i, account in enumerate(accounts):
            for acc in account[1:]:
                dic[acc].append(i)
        
        def dfs(i, emails):
            if vis[i]:
                return
            vis[i] = True
            for acc in accounts[i][1:]:
                emails.add(acc)
                for next_i in dic[acc]:
                    dfs(next_i, emails)
            return emails
        
        ret = []
        n = len(accounts)
        vis = [False] * n
        
        for i, account in enumerate(accounts):
            if vis[i]:
                continue
            
            emails = dfs(i, set())
            tmp = [account[0]] + sorted(emails)
            ret.append(tmp)
        
        return ret
        