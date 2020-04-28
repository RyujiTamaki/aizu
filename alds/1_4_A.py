def search(A, n, key):
    i = 0
    A[n] = key
    while A[i] != key:
        i += 1

    return i != n


n = int(input())
S = input().split()
S.append(None)
q = int(input())
T = input().split()

ans = 0
for key in T:
    if search(S, n, key):
        ans += 1

print(ans)
