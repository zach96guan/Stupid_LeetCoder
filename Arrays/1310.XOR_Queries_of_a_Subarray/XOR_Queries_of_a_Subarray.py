class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        for i in range(1, n):
            arr[i] ^= arr[i - 1]
        arr.insert(0, 0)
        
        ret = []
        for l, r in queries:
            ret.append(arr[r + 1] ^ arr[l])
        
        return ret
        