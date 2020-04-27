from collections import deque
import sys


class Process:
    def __init__(self, name, time):
        self._name = name
        self._time = time

    @property
    def name(self):
        return self._name

    @property
    def time(self):
        return self._time


input = sys.stdin.readline
N, q = map(int, input().split())

queue = deque()

for _ in range(N):
    s = input().split()
    p = Process(name=s[0], time=int(s[1]))
    queue.append(p)

elaps = 0
while len(queue) > 0:
    process = queue.popleft()
    c = min(q, process.time)
    process = Process(name=process.name, time=process.time - c)
    elaps += c
    if process.time > 0:
        queue.append(process)
    else:
        print(f"{process.name} {elaps}")
