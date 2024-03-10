class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        while self.stack1:
            top = self.stack1.pop()
            self.stack2.append(top)

        ans = self.stack2.pop()

        while self.stack2:
            top1 = self.stack2.pop()
            self.stack1.append(top1)

        return ans

    def peek(self) -> int:
        while self.stack1:
            top = self.stack1.pop()
            print(top)
            self.stack2.append(top)

        ans = self.stack2[-1]

        while self.stack2:
            top = self.stack2.pop()
            self.stack1.append(top)

        return ans

    def empty(self) -> bool:
        if len(self.stack1) == 0:
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()