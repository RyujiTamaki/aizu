from typing import List


def insertion_sort(A: List[int], g: int) -> int:
    cnt = 0
    for i in range(g, len(A)):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j -= g
            cnt += 1
        A[j + g] = v

    return cnt


def shell_sort(A: List[int], G: List[int]) -> int:
    cnt = 0
    for i in range(len(G) - 1, -1, -1):
        cnt += insertion_sort(A, G[i])

    return cnt


N = int(input())
A = []

for _ in range(N):
    A.append(int(input()))

G = []

h = 1
while h < N:
    G.append(h)
    h = 3 * h + 1

if N == 1:
    G.append(1)

cnt = shell_sort(A, G)

print(len(G))
print(" ".join([str(g) for g in reversed(G)]))

print(cnt)

for a in A:
    print(a)
