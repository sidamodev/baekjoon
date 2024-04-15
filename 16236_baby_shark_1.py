from heapq import heappush, heappop

d_ij = ((-1, 0), (0, -1), (0, 1), (1, 0))


def solve(baby_i, baby_j):
    baby_size = eat_count = 2
    time = 0
    pq = [(0, baby_i, baby_j)]
    visit = [[0] * N for _ in range(N)]
    while pq:
        d, baby_i, baby_j = heappop(pq)
        # 진행한 칸이 먹이인 경우
        if 0 < A[baby_i][baby_j] < baby_size:
            A[baby_i][baby_j] = 0
            eat_count -= 1
            time += d
            if eat_count == 0:
                baby_size += 1
                eat_count = baby_size
            # 초기화
            d = 0
            pq = []
            visit = [[0] * N for _ in range(N)]
        for di, dj in d_ij:
            baby_ni, baby_nj = baby_i + di, baby_j + dj
            # 조건 필터링 -> 맵 범위 / 방문체크 / 사이즈
            if not (0 <= baby_ni < N and 0 <= baby_nj < N): continue
            if visit[baby_ni][baby_nj]: continue
            if A[baby_ni][baby_nj] > baby_size: continue
            visit[baby_ni][baby_nj] = 1
            heappush(pq, (d + 1, baby_ni, baby_nj))
    return time


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
for i in range(N * N):
    if A[i // N][i % N] == 9:
        init_i, init_j = i // N, i % N
        A[i // N][i % N] = 0
        break
print(solve(init_i, init_j))