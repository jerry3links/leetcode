"""
    from DifficultyEasy.sol155MinStack import MinStack
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    a = obj.getMin()
    print("getMin(): {}".format(a))
    obj.pop()
    print("pop ...")
    a = obj.top()
    print("top: {}".format(a))
    a = obj.getMin()
    print("getMin(): {}".format(a))
"""
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x):
        if self.stack:
            self.stack.append(min(self.stack[-2], x))
        else:
            self.stack.append(x)
        self.stack.append(x)

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        if self.stack:

            return self.stack[-2]