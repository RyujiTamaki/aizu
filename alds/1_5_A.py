n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))


def dfs(i, total, t):
    if i == n:
        return total == t
    if dfs(i + 1, total, t):
        return True
    if dfs(i + 1, total + S[i], t):
        return True
    return False


for t in T:
    if dfs(0, 0, t):
        print("yes")
    else:
        print("no")
