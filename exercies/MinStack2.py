import sys

class Node:
    def __init__(self, value, min):
        self.value = value
        self.min = min

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values_stack = list()

    def push(self, x: int) -> None:
        if len(self.values_stack) > 0:
            if self.values_stack[-1].min > x:
                self.values_stack.append(Node(x, x))
            else:
                self.values_stack.append(Node(x, self.values_stack[-1].min))
        else:
            self.values_stack.append(Node(x, x))

    def pop(self) -> None:
        self.values_stack.pop()

    def top(self) -> int:
        return self.values_stack[-1].value

    def getMin(self) -> int:
        return self.values_stack[-1].min

minStack = MinStack()
minStack.push(2)
minStack.push(0)
minStack.push(3)
minStack.push(0)
print(minStack.getMin())
minStack.pop()
print(minStack.getMin())
minStack.pop()
print(minStack.getMin())
minStack.pop()
print(minStack.getMin())
minStack.pop()
print(minStack.getMin())

# minStack.push(-2)
# minStack.push(0)
# minStack.push(-3)
# minStack.push(103)
# minStack.push(-50)
# minStack.push(-70)
# minStack.push(-70)
# minStack.push(-70)
# print(minStack.values_stack)
# minStack.pop()
# minStack.pop()
# minStack.pop()
# minStack.pop()
#
# print(minStack.values_stack)
# print(minStack.top())
# print(minStack.getMin())
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

# minStack = MinStack()
# minStack.push(2147483646)
# print(minStack.values_stack)
# print(minStack.mins_stack)
# minStack.push(2147483646)
# print(minStack.values_stack)
# print(minStack.mins_stack)
# minStack.push(2147483647)
# print(minStack.values_stack)
# print(minStack.mins_stack)
# print(minStack.top())
# minStack.pop()
# print(minStack.values_stack)
# print(minStack.mins_stack)
# print(minStack.getMin())
# minStack.pop()
# print(minStack.values_stack)
# print(minStack.mins_stack)
# print(minStack.getMin())
# minStack.pop()
# print(minStack.values_stack)
# print(minStack.mins_stack)
# minStack.push(2147483647)
# print(minStack.values_stack)
# print(minStack.mins_stack)
# print(minStack.top())
# print(minStack.top())
# print(minStack.getMin())
# minStack.push(-2147483648)
# print(minStack.values_stack)
# print(minStack.mins_stack)
# print(minStack.top())
# print(minStack.getMin())
# minStack.pop()
# print(minStack.getMin())
