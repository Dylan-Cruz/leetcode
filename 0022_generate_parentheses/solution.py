from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN): 
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0,0)
        return res
    
    def generateAllPossibilities(self, n: int) -> List[str]:
        stack = []
        res = []
        runs = 0

        def backtrack(): 
            if run

            stack.append("(")
            backtrack()
            stack.pop()
             
            stack.append(")")
            backtrack()
            stack.pop()
    
solution = Solution()
print(solution.generateParenthesis(3))

