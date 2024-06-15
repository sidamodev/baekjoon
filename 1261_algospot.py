from heapq import heappush, heappop

M, N = map(int, input().split())
A = [list(input()) for _ in range(N)]

pq = [(0, 0, 0)]
visit = [[False] * M for _ in range(N)]
result = 0
while pq:
    c, i, j = heappop(pq)
    if (i, j) == (N - 1, M - 1):
        result = c
        break
    for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        if not (0 <= ni < N and 0 <= nj < M): continue
        if visit[ni][nj]: continue
        if A[ni][nj] == '0':
            heappush(pq, (c, ni, nj))
        elif A[ni][nj] == '1':
            A[ni][nj] = '0'
            heappush(pq, (c + 1, ni, nj))
        visit[ni][nj] = True
print(result)
