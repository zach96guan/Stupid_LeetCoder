class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nlogn), O(n)
        ret = []
        for start, end in sorted(intervals, key=lambda x:x[0]):
            if len(ret) > 0 and ret[-1][-1] >= start:
                ret[-1][-1] = max(ret[-1][-1], end)
            else:
                ret.append([start, end])
        return ret
    