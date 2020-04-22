def selection_sort(A):
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
A = list(map(int, input().split()))

sw = selection_sort(A)
A = [str(i) for i in A]
print(" ".join(A))
print(sw)
