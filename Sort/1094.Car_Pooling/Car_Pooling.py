class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # O(NlogN), O(N)
        lst = []
        
        for num, start, end in trips:
            lst.append((start, num))
            lst.append((end, -num))
        lst.sort()
        
        for _, num in lst:
            capacity -= num
            if capacity < 0:
                return False
        return True
        