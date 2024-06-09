from heapq import heappush, heappop

d_ij = [(-1, 0), (0, -1), (0, 1), (1, 0)]

N, M, F = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
taxi_i, taxi_j = map(int, input().split())
taxi_i -= 1
taxi_j -= 1
start_arr = []
dest_arr = []
chk = set()
for p_number in range(2, M + 2):
    start_i, start_j, dest_i, dest_j = map(int, input().split())
    start_arr.append((start_i - 1, start_j - 1))
    dest_arr.append((dest_i - 1, dest_j - 1))


def to_person():
    global taxi_i, taxi_j
    pq = [(0, taxi_i, taxi_j)]
    visited = [[0] * N for _ in range(N)]
    visited[taxi_i][taxi_j] = 1
    while pq:
        d, i, j = heappop(pq)
        if arr[i][j] == 0:  # 승객을 찾으면 승객 번호와 소모된 연료를 반환
            for p in range(M):
                if p not in chk and start_arr[p] == (i, j):
                    taxi_i, taxi_j = i, j
                    chk.add(p)
                    return d, p
        for di, dj in d_ij:
            ni, nj = i + di, j + dj
            if not (0 <= ni < N and 0 <= nj < N): continue
            if visited[ni][nj] or arr[ni][nj] == 1: continue
            visited[ni][nj] = 1
            heappush(pq, (d + 1, ni, nj))
    return 'error'


def to_dest(p_n):
    global taxi_i, taxi_j
    pq = [(0, taxi_i, taxi_j)]
    visited = [[0] * N for _ in range(N)]
    visited[taxi_i][taxi_j] = 1
    while pq:
        d, i, j = heappop(pq)
        if dest_arr[p_n] == (i, j):
            taxi_i, taxi_j = i, j
            return d
        for di, dj in d_ij:
            ni, nj = i + di, j + dj
            if not (0 <= ni < N and 0 <= nj < N): continue
            if visited[ni][nj] or arr[ni][nj] == 1: continue
            visited[ni][nj] = 1
            heappush(pq, (d + 1, ni, nj))
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
    if F <= p_dist or F - p_dist - d_dist < 0:
        F = -1
        break
    F = F - p_dist + d_dist

print(F)
