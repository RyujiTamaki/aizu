from typing import List


def selection_sort(A: List[int]):
    sw = 0
    for i in range(len(A) - 1):
        minj = i

        for j in range(i, len(A)):
            if A[j] < A[minj]:
                minj = j

        A[i], A[minj] = A[minj], A[i]

        if i != minj:
            sw += 1

    return sw


N = input()
A: List[int] = list(map(int, input().split()))

sw = selection_sort(A)
str_A: List[str] = [str(i) for i in A]
print(" ".join(str_A))
print(sw)
