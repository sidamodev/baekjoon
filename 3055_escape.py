from collections import deque

R, C = map(int, input().split())
forest = [list(input()) for _ in range(R)]

visited = [[0] * C for _ in range(R)]
q = deque([])
s_i, s_j = 0, 0
for r in range(R):
    for c in range(C):
        value = forest[r][c]
        if value == '*':
            q.append((r, c, value))
        elif value == 'S':
            s_i, s_j = r, c
q.append((s_i, s_j, 'S'))


def bfs():
    while q:
        i, j, v = q.popleft()
        if forest[i][j] == 'D':
            return visited[i][j]
        for ni, nj in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
            if not (0 <= ni < R and 0 <= nj < C): continue
            if forest[ni][nj] == 'X': continue
            if v == '*' and forest[ni][nj] in ('S', '.'):
                forest[ni][nj] = '*'
                q.append((ni, nj, v))
            if v == 'S' and forest[ni][nj] != '*' and not visited[ni][nj]:
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni, nj, v))
    return 'KAKTUS'


print(bfs())
