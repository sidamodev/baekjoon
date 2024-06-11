from heapq import heappush, heappop


def input_list():
    return map(int, input().split())


N, M, F = input_list()
arr = [list(input_list()) for _ in range(N)]
taxi = tuple(map(lambda x: x - 1, input_list()))
dest_dict = {}
for p_number in range(2, M + 2):
    start_i, start_j, dest_i, dest_j = (map(lambda x: x - 1, input_list()))
    arr[start_i][start_j] = 2
    dest_dict[(start_i, start_j)] = (dest_i, dest_j)


def get_dist(F, fuel_empty, is_target):
    global taxi
    pq = [(0, taxi[0], taxi[1])]
    visit = [[False] * N for _ in range(N)]
    while pq:
        d, i, j = heappop(pq)
        if visit[i][j]: continue
        visit[i][j] = True
        if is_target(i, j):
            if fuel_empty(d, F):
                return -1
            arr[i][j] = 0
            taxi = (i, j)
            return d
        for ni, nj in ((i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)):
            if not (0 <= ni < N and 0 <= nj < N): continue
            if arr[ni][nj] == 1: continue
            heappush(pq, (d + 1, ni, nj))
    return -1


for k in range(M):
    p_dist = get_dist(F, lambda dist, fuel: dist >= fuel, lambda x, y: arr[x][y] == 2)
    if p_dist == -1:
        F = -1
        break
    F -= p_dist
    t_i, t_j = taxi
    d_dist = get_dist(F, lambda dist, fuel: dist > fuel, lambda x, y: dest_dict[(t_i, t_j)] == (x, y))
    if d_dist == -1:
        F = -1
        break
    F += d_dist
print(F)
