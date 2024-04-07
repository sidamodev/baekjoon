from collections import deque

d_ij = ((-1, 0), (0, -1), (0, 1), (1, 0))
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * N for _ in range(N)]
size = exp = 2
pos_i = pos_j = t = 0
for i in range(N * N):
    if A[i // N][i % N] == 9:
        pos_i, pos_j = i // N, i % N
        break

queue = deque([(pos_i, pos_j)])
while queue:
    i, j = queue.popleft()
    print(i, j)
    for di, dj in d_ij:
        ni, nj = i + di, j + dj
        if not (0 <= ni < N and 0 <= nj < N) or (A[ni][nj] > size): continue
        v[ni][nj] = 1
        if A[ni][nj] == 0 or A[ni][nj] == size:
            t += 1
            queue.append((ni, nj))
        elif A[ni][nj] < size:
            A[ni][nj] = 0
            t += 1
            exp -= 1
            if exp == 0:
                size += 1
                exp = size
            queue.append((ni, nj))
            break
