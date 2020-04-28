def binary_search(A, n, key):
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if A[mid] == key:
            return True
        elif key < A[mid]:
            right = mid
        else:
            left = mid + 1
    return False


n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

ans = 0
for key in T:
    if binary_search(S, n, key):
        ans += 1

print(ans)
