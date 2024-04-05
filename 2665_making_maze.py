from heapq import heappush, heappop
import pprint

N = int(input())
R = [list(map(int, input())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
d_ij = ((0, 1), (0, -1), (-1, 0), (1, 0))
queue = deque([(0, 0)])
cnt = 0
while queue:
    i, j = queue.popleft()
    for di, dj in d_ij:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N:
            if visit[ni][nj] == 1: continue
            if R[ni][nj] == 1:
                visit[ni][nj] = 1
                queue.append((ni, nj))
            elif R[ni][nj] == 0:
                visit[ni][nj] = 1
                cnt += 1
                queue.append((ni, nj))
print(cnt)