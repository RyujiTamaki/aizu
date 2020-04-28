n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))
dp = set()


def dfs(i, total):
    dp.add(total)
    if i == n:
        return None
    dfs(i + 1, total)
    dfs(i + 1, total + S[i])
    return None


dfs(0, 0)

for t in T:
    if t in dp:
        print("yes")
    else:
        print("no")
