import collections

class Window:
    def __init__(self):
        self.dic = collections.Counter()
        self.count = 0
    
    def add(self, num):
        self.dic[num] += 1
        if self.dic[num] == 1:
            self.count += 1
    
    def remove(self, num):
        self.dic[num] -= 1
        if self.dic[num] == 0:
            self.count -= 1
        

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        # sliding window, O(N), O(N)
        w1, w2 = Window(), Window()
        ret = l1 = l2 = 0  # monotonously increeasing l1 and l2
        
        for r, num in enumerate(A):
            w1.add(num)
            w2.add(num)
            
            while w1.count >= K + 1:
                w1.remove(A[l1])
                l1 += 1
            while w2.count >= K:
                w2.remove(A[l2])
                l2 += 1
            
            ret += l2 - l1
        return ret
        