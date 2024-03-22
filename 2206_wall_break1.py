import sys
from collections import deque
input = sys.stdin.readline
d_ij = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(s_i, s_j):
    q = deque([(s_i, s_j, 1, 1)])
    v1[0][0] = 1
    while q:
        i, j, b, d = q.popleft()
        if (i, j) == (N - 1, M - 1):
            return d
        for di, dj in d_ij:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if not b and not v2[ni][nj] and not v1[ni][nj] and A[ni][nj] == '0':
                    v2[ni][nj] = d + 1
                    q.append((ni, nj, 0, d + 1))
                if b and not v1[ni][nj]:
                    v1[ni][nj] = d + 1
                    if A[ni][nj] == '1':
                        q.append((ni, nj, 0, d + 1))
                    else:
                        q.append((ni, nj, 1, d + 1))
    return -1


N, M = map(int, input().split())
A = [input().strip() for _ in range(N)]
v1, v2 = [[0] * M for _ in range(N)], [[0] * M for _ in range(N)]
print(bfs(0, 0))
