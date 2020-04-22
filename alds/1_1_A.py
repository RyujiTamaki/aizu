from typing import List


def trace(A: List[int]):
    a = " ".join([str(i) for i in A])
    print(a)
    return None


def insertion_sort(A: List[int]):
    S = A.copy()
    for i in range(1, len(A)):
        v = S[i]
        j = i - 1
        while j >= 0 and S[j] > v:
            S[j + 1] = S[j]
            j -= 1
        S[j + 1] = v
        trace(S)
    return None


N = input()
A: List[int] = list(map(int, input().split()))

trace(A)
insertion_sort(A)
