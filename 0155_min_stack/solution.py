class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            current_min = self.getMin()
            if val < current_min:
                self.stack.append((val, val))
            else:
                self.stack.append((val, current_min))

        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

    def __str__(self):
        return str(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

stack = MinStack()
stack.push(-2)
stack.push(0)
stack.push(-3)
print(stack)
print(stack.getMin())
stack.pop()
print(stack.top())
print(stack.getMin())
