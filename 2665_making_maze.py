from collections import deque

N = int(input())
R = [list(map(int, input())) for _ in range(N)]
visit = [[[0, 0] for _ in range(N)] for _ in range(N)]
d_ij = ((0, 1), (0, -1), (-1, 0), (1, 0))
queue = deque([(0, 0)])
result = 0
while queue:
    i, j = queue.popleft()
    for di, dj in d_ij:
        ni, nj = i + di, j + dj
        if not (0 <= ni < N and 0 <= nj < N): continue
        if visit[ni][nj][0] == 0 or visit[i][j][1] + 1 <= visit[ni][nj][1]:
            if R[ni][nj] == 1:
                visit[ni][nj][0] = 1
                visit[ni][nj][1] = visit[i][j][1]
                queue.append((ni, nj))
            elif R[ni][nj] == 0:
                visit[ni][nj][0] = 1
                visit[ni][nj][1] = visit[i][j][1] + 1
                queue.append((ni, nj))
print(visit[N - 1][N - 1][1])
