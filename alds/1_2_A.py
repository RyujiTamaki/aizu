def bubble_sort(A):
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
A = list(map(int, input().split()))

sw = bubble_sort(A)
A = [str(i) for i in A]
print(" ".join(A))
print(sw)
