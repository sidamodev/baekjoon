from heapq import heappush, heappop

d_ij = [(0, 1), (1, 0), (-1, 0), (0, -1)]
W, H = map(int, input().split())
A = [list(input()) for _ in range(H)]
M = [(i, j) for i in range(H) for j in range(W) if A[i][j] == 'C']
result = []
pq = [(0, M[0][0], M[0][1], 5)]
visit = set()
while pq:
    w, i, j, d = heappop(pq)
    if (i, j, d) in visit: continue
    if (i, j) == M[1]:
        result = w
        break
    visit.add((i, j, d))
    for d_idx, (di, dj) in enumerate(d_ij):
        ni, nj = i + di, j + dj
        if not (0 <= ni < H and 0 <= nj < W): continue
        if A[ni][nj] == '*': continue
        if (ni, nj, d_idx) in visit: continue
        if d == d_idx:
            heappush(pq, (w, ni, nj, d_idx))
        else:
            heappush(pq, (w + 1, ni, nj, d_idx))

print(result - 1)
