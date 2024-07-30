class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 != 0:
            return False
        
        stack = []

        for i in range(len(s)):

            if(s[i] == '(' or s[i] == '{' or s[i] == '['):
                stack.append(s[i])
                print(s[i])

            if(len(stack) == 0):
                return False

            if(s[i] == ')' and stack.pop() != '('):
                return False
            if(s[i] == '}' and stack.pop() != '{'):
                return False
            if(s[i] == ']' and stack.pop() != '['):
                return False
        
        if(len(stack) != 0):
            return False
        return True