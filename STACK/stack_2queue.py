class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) != 0:
            top = self.q1.pop()
            self.q2.append(top)

        ans = self.q2.pop(0)

        while len(self.q2) != 0:
            top = self.q2.pop()
            self.q1.append(top)

        return ans

    def top(self) -> int:
        while len(self.q1) != 0:
            top = self.q1.pop()
            self.q2.append(top)

        ans = self.q2[0]

        while len(self.q2) != 0:
            top1 = self.q2.pop()
            self.q1.append(top1)

        return ans

    def empty(self) -> bool:
        if len(self.q1) == 0:
            return True
        else:
            return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()