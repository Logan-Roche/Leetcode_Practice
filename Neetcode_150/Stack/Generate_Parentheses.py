class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # only add open paranthesis if openN < n
        # only add a closing paranthesis if closedN < openN
        # valid if open == closed == n

        stack = []
        result = []

        def recursive(openN, closedN):
            if (closedN == openN == n):
                result.append("".join(stack))
                return
            
            if(openN < n):
                stack.append("(")
                recursive(openN + 1, closedN)
                stack.pop()
            
            if(closedN < openN):
                stack.append(")")
                recursive(openN, closedN + 1)
                stack.pop()
        
        recursive(0, 0)
        return result
            



        
        