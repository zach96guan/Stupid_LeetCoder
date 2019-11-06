class Solution:
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # Sort the envelopes first by increasing width
        # For each block of same-width envelopes, sort by decreasing height
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # Then LIS
        dp = [0] * len(envelopes)
        res = 0
        for env in envelopes:
            if res == 0 or env[1] > dp[res-1]:  # early check
                dp[res] = env[1]
                res += 1
            else:
                l, r = 0, res-1
                while l != r:
                    m = int((l + r) / 2)
                    if dp[m] < env[1]:
                        l = m + 1
                    else:
                        r = m
                dp[l] = env[1]
                
        return res
    