class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '*', '/']
        stack = []
        
        for tok in tokens:
            if tok not in ops:
                stack.append(int(tok))
            
            else:
                pre = stack.pop()
                if tok == '+':
                    stack[-1] += pre
                elif tok == '-':
                    stack[-1] -= pre
                elif tok =='*':
                    stack[-1] *= pre
                else:
                    stack[-1] = int(stack[-1] / pre)  # different from //= pre, when pre < 0

        return stack[0]
        