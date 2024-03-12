import sys

input = sys.stdin.readline
T = int(input())
d_ij = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def dfs(i, j):
    stk = [(i, j)]
    while stk:
        p, q = stk.pop()
        A[p][q] = 0
        for di, dj in d_ij:
            ni, nj = p + di, q + dj
            if 0 <= ni < N and 0 <= nj < M and A[ni][nj]:
                stk.append((ni, nj))

for _ in range(T):
    M, N, K = map(int, input().split())
    A = [[0] * M for _ in range(N)]
    cnt = 0
    for i in range(K):
        a, b = map(int, input().split())
        A[b][a] = 1
    for i in range(N):
        for j in range(M):
            if A[i][j]:
                dfs(i, j)
                cnt += 1
    print(cnt)
