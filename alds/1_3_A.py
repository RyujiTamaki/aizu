from typing import List

stack: List[int] = []


for s in input().split():
    if s == "+":
        a = int(stack.pop())
        b = int(stack.pop())
        stack.append(a + b)
    elif s == "-":
        b = int(stack.pop())
        a = int(stack.pop())
        stack.append(a - b)
    elif s == "*":
        a = int(stack.pop())
        b = int(stack.pop())
        stack.append(a * b)
    else:
        stack.append(int(s))

print(stack.pop())
