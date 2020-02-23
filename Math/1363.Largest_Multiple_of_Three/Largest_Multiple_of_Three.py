class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        # math
        n, s = len(digits), sum(digits)
        
        def helper(nums):
            return "".join(map(str, sorted(digits, reverse=True)))

        if not digits or not n:
            return ""
        if s == 0:
            return "0"
        if s % 3 == 0:
            return helper(digits)
        
        digits.sort()
        r = s % 3
        to_delete = [-1] * 2
        
        if r == 1:
            for i in range(n):
                if digits[i] % 3 == 1:
                    digits.pop(i)
                    return helper(digits)
                
                if digits[i] % 3 == 2:
                    if to_delete[0] == -1:
                        to_delete[0] = i
                    elif to_delete[1] == -1:
                        to_delete[1] = i
            
            if to_delete[0] != -1 and to_delete[1] != -1:
                digits = [digits[i] for i in range(n) if i not in to_delete]
                return helper(digits)

        elif r == 2:
            for i in range(n):
                if digits[i] % 3 == 2:
                    digits.pop(i)
                    return helper(digits)
                
                if digits[i] % 3 == 1:
                    if to_delete[0] == -1:
                        to_delete[0] = i
                    elif to_delete[1] == -1:
                        to_delete[1] = i
            
            if to_delete[0] != -1 and to_delete[1] != -1:
                digits = [digits[i] for i in range(n) if i not in to_delete]
                return helper(digits)
  
