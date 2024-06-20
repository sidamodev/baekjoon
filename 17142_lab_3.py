from collections import deque

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
virus = []

for r in range(N):
    for c in range(N):
        if A[r][c] == 2:
            virus.append((r, c))


# 0 빈칸 1 벽 2 비활성 3 활성
def diffusion(v_arr):
    lab = [x[:] for x in A]
    for v_i, v_j in v_arr:
        lab[v_i][v_j] = 3

    q = deque(v_arr)
    visit = [[0] * N for _ in range(N)]
    while q:
        i, j = q.popleft()
        for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if not (0 <= ni < N and 0 <= nj < N): continue
            if visit[ni][nj] or (lab[ni][nj] != 0 and lab[ni][nj] != 2): continue
            if lab[ni][nj] == 0:
                lab[ni][nj] = 3
            visit[ni][nj] = visit[i][j] + 1
            q.append((ni, nj))

    t = 0
    for i in range(N):
        for j in range(N):
            if lab[i][j] == 0:
                return int(1e9)
            if lab[i][j] == 3:
                if visit[i][j] > t:
                    t = visit[i][j]
    return t


V = len(virus)
chk = []
min_time = int(1e9)


def dfs(i, j):
    global min_time
    if i == M:
        time = diffusion(chk)
        if time < min_time:
            min_time = time
        return
    for k in range(j, V):
        chk.append(virus[k])
        dfs(i + 1, k + 1)
        chk.pop()


dfs(0, 0)
print(min_time if min_time != int(1e9) else -1)
