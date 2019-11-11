class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        nums = [dic[ch] for ch in s]
        max_num, ret = float('-inf'), 0
        
        for num in nums[::-1]:
            if num < max_num:
                ret -= num
            else:
                max_num = num
                ret += num
        
        return ret
        