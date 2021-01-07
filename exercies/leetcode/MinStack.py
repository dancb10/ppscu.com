import sys

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = sys.maxsize
        self.mins_stack = list()
        self.values_stack = list()

    def push(self, x: int) -> None:
        if x <= self.min:
            self.min = x
            self.mins_stack.append(x)
        self.values_stack.append(x)

    def pop(self) -> None:
        toPop = self.values_stack[-1]
        if toPop == self.min and not self.mins_stack:
            self.mins_stack.pop()
            self.min = self.mins_stack[-1]
        self.values_stack.pop()

    def top(self) -> int:
        return self.values_stack[-1]

    def getMin(self) -> int:
        return self.min

# minStack = MinStack()
# minStack.push(-2)
# minStack.push(0)
# minStack.push(-3)
# minStack.push(103)
# minStack.pop()
# print(minStack.values_stack)
# minStack.push(-6)
# minStack.push(5)
# minStack.push(-2)
# minStack.pop()
# minStack.push(-5)
# print(minStack.values_stack)
# print(minStack.top())
# print(minStack.getMin())
# minStack.pop()
# print(minStack.values_stack)
# print(minStack.top())
# print(minStack.getMin())

# minStack = MinStack()
# minStack.push(0)
# minStack.push(1)
# minStack.push(0)
# print(minStack.getMin())
# minStack.pop()
# print(minStack.getMin())

minStack = MinStack()
minStack.push(2147483646)
print(minStack.values_stack)
print(minStack.mins_stack)
minStack.push(2147483646)
print(minStack.values_stack)
print(minStack.mins_stack)
minStack.push(2147483647)
print(minStack.values_stack)
print(minStack.mins_stack)
print(minStack.top())
minStack.pop()
print(minStack.values_stack)
print(minStack.mins_stack)
print(minStack.getMin())
minStack.pop()
print(minStack.values_stack)
print(minStack.mins_stack)
print(minStack.getMin())
minStack.pop()
print(minStack.values_stack)
print(minStack.mins_stack)
minStack.push(2147483647)
print(minStack.values_stack)
print(minStack.mins_stack)
print(minStack.top())
print(minStack.top())
print(minStack.getMin())
minStack.push(-2147483648)
print(minStack.values_stack)
print(minStack.mins_stack)
print(minStack.top())
print(minStack.getMin())
minStack.pop()
print(minStack.getMin())
