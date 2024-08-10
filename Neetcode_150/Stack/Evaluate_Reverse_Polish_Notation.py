class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # Stack, if number then do nothing, if operator then use
        # number in stack, when done remove numbers and add
        # resulting value.

        stack = []

        for tok in tokens:
            print(stack)
            if(tok == "+"):
                val = stack.pop() + stack.pop()
                stack.append(val)
            elif(tok == "-"):
                a, b= stack.pop(), stack.pop()
                stack.append(b - a)
            elif(tok == "*"):
                val = stack.pop() * stack.pop()
                stack.append(val)
            elif(tok == "/"):
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(tok))
        
        return int(stack[0])
                


        