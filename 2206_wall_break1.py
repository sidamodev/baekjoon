import sys
from collections import deque

input = sys.stdin.readline


def bfs(s_i, s_j):
    global wall_break
    q = deque([(s_i, s_j)])
    A[s_i][s_j] = 1
    while q:
        i, j = q.popleft()
        for di, dj in d_ij:
            ni, nj = i + di, j + dj
            if N > ni >= 0 <= nj < M:
                if wall_break:
                    if (i, j) == (N - 1, M - 1):
                        wall_break = 0
                    else:
                        bfs(ni, nj)
                if A[ni][nj] == 0:
                    A[ni][nj] = A[i][j] + 1
                    q.append((ni, nj))


N, M = map(int, input().split())
A = [list(map(int, input().strip())) for _ in range(N)]
d_ij = [(0, 1), (1, 0), (0, -1), (-1, 0)]
wall_break = 1
bfs(0, 0)
res = A[N - 1][M - 1]
if not res:
    res = -1
print(res)
