N, M = map(int, input().split())
maze = [input() for _ in range(N)]

mov_dict = {
    'U': (-1, 0),
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1),
}

visited = [[0] * M for _ in range(N)]


# 방문배열 Flag
# 0 : 미방문
# 1 : 방문
# 2 : 탈출 불가능한 경로
# 3 : 탈출 가능한 경로

def chk_escape(p, q):
    trace = set()
    while True:
        visited[p][q] = 1
        trace.add((p, q))
        (np, nq) = tuple(sum(elem) for elem in zip((p, q), mov_dict[maze[p][q]]))
        if not (0 <= np < N and 0 <= nq < M) or visited[np][nq] == 3:
            # 경로 모두 3으로 처리
            update_visit(trace, 3)
            return 1
        elif visited[np][nq] == 1 or visited[np][nq] == 2:
            # 경로 모두 2로 처리
            update_visit(trace, 2)
            return 0
        p, q = np, nq


def update_visit(trace_set, value):
    for r, c in trace_set:
        visited[r][c] = value


total_sum = 0
for i in range(N):
    for j in range(M):
        total_sum += chk_escape(i, j)

print(total_sum)
