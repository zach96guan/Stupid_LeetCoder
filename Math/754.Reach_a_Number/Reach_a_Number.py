class Solution:
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        # O(sqrt(target)), O(1)
        target = abs(target)
        pos = 0
        while target > 0:
            pos += 1
            target -= pos
        
        return pos if target % 2 == 0 else (pos + 1) + pos % 2
        