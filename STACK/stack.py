class Stack:
    def __init__(self, n: int):
        # Write your code here
        # n is the size of stack
        self.n=n
        self.stack=[]

    def push(self, num: int):
        # num is the value that needs to be inserted
        if len(self.stack)!=self.n:
            self.stack.append(num)

    def pop(self) -> int:
        # Write your code here
        if len(self.stack)!=0:
            ans=self.stack.pop()
            return ans
        else:
            return -1

    def top(self) -> int:
        # Write your code here
        if len(self.stack)!=0:
            return self.stack[-1]
        else:
            return -1

    def isEmpty(self) -> int:
        # Write your code here
        if len(self.stack)==0:
            return 1
        else:
            return 0

    def isFull(self) -> int:
        # Write your code here
        if len(self.stack)==self.n:
            return 1
        else:
            return 0
