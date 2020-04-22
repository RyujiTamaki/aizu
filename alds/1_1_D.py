from typing import List


n: int = int(input())
R: List[int] = []

for _ in range(n):
    R.append(int(input()))

maxv: int = R[1] - R[0]
minv: int = R.pop(0)

for r in R:
    maxv = max(maxv, r - minv)
    minv = min(minv, r)

print(maxv)
