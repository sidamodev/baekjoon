from collections import deque

d_ij = [(0, 1), (1, 0), (0, -1), (-1, 0)]


# 새 배열 만들어서 기록하고 나중에 반영
def diffusion(a, b):
    queue = deque([(a, b)])
    while queue:
        r, c = queue.popleft()
        if A[r][c] == 0 or (r, c) == (c_i, c_j) or (r, c) == (c_i + 1, c_j): continue
        L = 0
        dust = A[r][c] // 5
        for di, dj in d_ij:
            nr, nc = r + di, c + dj
            if not (0 <= nr < R and 0 <= nc < C) or (nr, nc) == (c_i, c_j) or (nr, nc) == (c_i + 1, c_j): continue
            B[nr][nc] = B[nr][nc] + dust
            queue.append((nr, nc))
            L += 1
        B[r][c] -= L * dust



R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
B = [[0] * C for _ in range(R)]

# 공청기 위치
c_i = c_j = 0
for i in range(R * C):
    if A[i // C][i % C] == -1:
        c_i = i // C
        c_j = i % C
        break

for i in range(T):
