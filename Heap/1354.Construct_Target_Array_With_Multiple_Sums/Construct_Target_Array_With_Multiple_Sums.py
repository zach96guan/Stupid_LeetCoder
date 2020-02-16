class Solution:
    def isPossible(self, target: List[int]) -> bool:
        # backtrack
        if target == [1] * len(target):
            return True
        
        total = sum(target)
        while True:
            num = max(target)
            idx = target.index(num)
            
            if num == 1: 
                return True
            
            total -= num
            num -= total
            total += num
            
            if num <= 0: 
                return False
            
            target[idx] = num
        