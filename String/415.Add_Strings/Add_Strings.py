class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        lst1, lst2 = list(num1), list(num2)
        ret = []
        c = 0
        
        while lst1 or lst2 or c:
            tmp1 = lst1.pop() if lst1 else '0'
            tmp2 = lst2.pop() if lst2 else '0'
            cur = c + ord(tmp1) - ord('0') + ord(tmp2) - ord('0')
            
            c, cur = divmod(cur, 10)
            ret.append(str(cur))

        return ''.join(ret[::-1])
        