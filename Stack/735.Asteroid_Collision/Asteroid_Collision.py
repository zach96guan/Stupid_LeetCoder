class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        # O(N), O(N)
        stack = []
        
        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                if stack[-1] < -a:
                    stack.pop()
                    continue
                
                elif stack[-1] + a == 0:
                    stack.pop()
                
                break

            else:
                stack.append(a)
        
        return stack
        
        