class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if(len(self.stack) == 1):
            self.minStack.append(val)
        elif(val < self.minStack[-1]):
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])
        

    def pop(self) -> None:
        self.stack.pop(-1)
        self.minStack.pop(-1)
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
