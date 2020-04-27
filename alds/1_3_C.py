from collections import deque
import sys


input = sys.stdin.readline

n = int(input())
doubly_linked_list = deque()

for i in range(n):
    command = input().rstrip()
    if command[0] == "i":
        doubly_linked_list.appendleft(command[7:])
    elif command[6] == "F":
        doubly_linked_list.popleft()
    elif command[6] == "L":
        doubly_linked_list.pop()
    else:
        try:
            doubly_linked_list.remove(command[7:])
        except ValueError:
            pass

print(" ".join(map(str, doubly_linked_list)))
