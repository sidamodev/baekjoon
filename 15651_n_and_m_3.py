N, M = map(int, input().split())
path = []
chk = [0] * (N + 1)

def dfs(i):
    if i == M:
        print(' '.join(map(str, path)))
        return
    for k in range(1, N + 1):
        path.append(k)
        dfs(i + 1)
        path.pop()

dfs(0)