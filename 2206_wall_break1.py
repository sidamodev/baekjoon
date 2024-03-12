import sys
from collections import deque

input = sys.stdin.readline
d_ij = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(s_i, s_j, w_b):
    q = deque([(s_i, s_j)])
    visit[s_i][s_j] = 1
    while q:
        i, j = q.popleft()
        for di, dj in d_ij:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if not visit[ni][nj] and A[ni][nj] == 0:
                    visit[ni][nj] = visit[i][j] + 1
                    q.append((ni, nj))
                    print(visit)

            # elif w_b and not visit[ni][nj] and A[ni][nj] == 1:
            #     bfs(ni, nj, 0)

    # tmp = visit[N - 1][M - 1]
    # if tmp > 0:
    #     v.append(tmp)


N, M = map(int, input().split())
A = [list(map(int, input().strip())) for _ in range(N)]
v = []
visit = [[0] * M for _ in range(N)]

bfs(0, 0, 1)
res = -1
if v:
    res = min(v) + 1
print(v)
