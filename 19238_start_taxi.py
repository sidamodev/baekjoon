from collections import deque
import pprint

d_ij = [(-1, 0), (0, -1), (1, 0), (0, 1)]

# NxM, Fuel
N, M, F = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
taxi_i, taxi_j = map(int, input().split())
taxi_i -= 1
taxi_j -= 1
for p_number in range(2, M + 2):
    start_i, start_j, dest_i, dest_j = map(int, input().split())
    arr[start_i - 1][start_j - 1] = p_number
    arr[dest_i - 1][dest_j - 1] = -p_number

pprint.pprint(arr)


def to_person():
    global taxi_i, taxi_j, F
    q = deque([(taxi_i, taxi_j)])
    visited = [[0] * N for _ in range(N)]
    visited[taxi_i][taxi_j] = 1
    while q:
        i, j = q.popleft()
        if arr[i][j] > 1:  # 승객을 찾으면 승객 번호와 소모된 연료를 반환
            tmp_num = arr[i][j]
            arr[i][j] = 0
            taxi_i, taxi_j = i, j
            return visited[i][j] - 1, tmp_num
        for di, dj in d_ij:
            ni, nj = i + di, j + dj
            if not (0 <= ni < N and 0 <= nj < N): continue
            if visited[ni][nj] or arr[ni][nj] == 1: continue
            visited[ni][nj] = visited[i][j] + 1
            q.append((ni, nj))
    return 'error'


def to_dest(p_n):
    global taxi_i, taxi_j, F
    q = deque([(taxi_i, taxi_j)])
    visited = [[0] * N for _ in range(N)]
    visited[taxi_i][taxi_j] = 1
    while q:
        i, j = q.popleft()
        if arr[i][j] == -p_n:
            arr[i][j] = 0
            taxi_i, taxi_j = i, j
            return visited[i][j] - 1
        for di, dj in d_ij:
            ni, nj = i + di, j + dj
            if not (0 <= ni < N and 0 <= nj < N): continue
            if visited[ni][nj] or arr[ni][nj] == 1: continue
            visited[ni][nj] = visited[i][j] + 1
            q.append((ni, nj))
    return 'error'


for k in range(M):
    tmp = to_person()
    if tmp == 'error':
        F = -1
        break
    p_dist, p_num = tmp
    d_dist = to_dest(p_num)
    if d_dist == 'error':
        F = -1
        break
    if F - p_dist <= 0 or F - p_dist - d_dist < 0:
        F = -1
        break
    F = F - p_dist + d_dist

print(F)
