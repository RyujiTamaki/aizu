from typing import List


def bubble_sort(A: List[int]):
    sw = 0
    flag = True
    i = 0

    while flag:
        flag = False
        for j in range(len(A) - 1, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
                flag = True
                sw += 1
        i += 1

    return sw


N = input()
A: List[int] = list(map(int, input().split()))

sw = bubble_sort(A)
str_A: List[str] = [str(i) for i in A]
print(" ".join(str_A))
print(sw)
