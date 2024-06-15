N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

house, store = [], []

for i in range(N):
    for j in range(N):
        if A[i][j] == 1:
            house.append((i, j))
        elif A[i][j] == 2:
            store.append((i, j))


def total_dist(picked_store):
    sum_dist = 0
    for house_i, house_j in house:
        min_dist = int(1e9)
        for store_i, store_j in picked_store:
            dist = abs(house_i - store_i) + abs(house_j - store_j)
            if dist < min_dist:
                min_dist = dist
        sum_dist += min_dist
    return sum_dist


picked_store = []
result = int(1e9)


def dfs(lev, j):
    global result
    if lev == M + 1:
        return
    for k in range(j, len(store)):
        picked_store.append(store[k])
        cur = total_dist(picked_store)
        if cur < result:
            result = cur
        dfs(lev + 1, k + 1)
        picked_store.pop()


dfs(1, 0)
print(result)
