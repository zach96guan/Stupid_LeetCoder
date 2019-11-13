class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        # O(N)
        if str1 == str2:
            return True
        
        dic = {}
        for i, j in zip(str1, str2):
            if i in dic and dic[i] != j:
                return False
            dic[i] = j
        
        return len(set(str2)) < 26
        