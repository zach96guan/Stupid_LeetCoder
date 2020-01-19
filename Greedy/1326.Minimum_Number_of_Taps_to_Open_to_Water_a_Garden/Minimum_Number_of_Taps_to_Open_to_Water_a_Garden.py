class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # greedy, jump game 2
        if not any(ranges):
            return -1
        
        arr = [0] * (n + 1)
        for i, d in enumerate(ranges):
            l = max(i - d, 0)
            r = min(i + d, n)
            arr[l] = max(arr[l], r)

        ret = 0
        pos, nxt_pos = arr[0], 0
        for i, d in enumerate(arr):
            nxt_pos = max(nxt_pos, d)
            if i == pos:
                pos = nxt_pos
                ret += 1
            
            if pos < i:
                return -1
        
        return ret

        