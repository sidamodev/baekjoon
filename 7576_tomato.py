from collections import deque

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]


def find_day():
    result = 0
    for i in range(N):
        for j in range(M):
            if not box[i][j]:
                result = -1
                return result
            elif box[i][j] > result:
                result = box[i][j]
    return result - 1

`
d_ij = [(0, 1), (1, 0), (0, -1), (-1, 0)]
start_lst = [(i, j) for i in range(N) for j in range(M) if box[i][j] == 1]
q = deque(start_lst)
while q:
    i, j = q.popleft()
    for di, dj in d_ij:
        ni, nj = i + di, j + dj
        if N > ni >= 0 <= nj < M:
            if box[ni][nj] == 0:
                box[ni][nj] = box[i][j] + 1
                q.append((ni, nj))

print(find_day())
