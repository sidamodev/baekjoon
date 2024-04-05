d_ij = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def diffusion(r, c):
    dust = A[r][c] // 5
    L = 0
    for di, dj in d_ij:
        nr, nc = r + di, c + dj
        if not (0 <= nr < R and 0 <= nc < C) or (nr, nc) == (c_i, c_j) or (nr, nc) == (c_i + 1, c_j): continue
        B[nr][nc] += dust
        L += 1
    B[r][c] -= L * dust


R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]

# 공청기 위치
c_i = c_j = 0
for i in range(R):
    if A[i][0] == -1:
        c_i = i
        break

for p in range(T):
    B = [[0] * C for _ in range(R)]
    # 확산
    for i in range(R):
        for j in range(C):
            if A[i][j] > 0:
                diffusion(i, j)
    # 원 배열에 반영
    for i in range(R):
        for j in range(C):
            A[i][j] += B[i][j]

    # 공기청정기
    # 위
    for j in range(c_i, 0, -1):
        A[j][0] = A[j - 1][0]
    for j in range(C - 1):
        A[0][j] = A[0][j + 1]
    for j in range(c_i):
        A[j][C - 1] = A[j + 1][C - 1]
    for j in range(C - 1, 1, -1):
        A[c_i][j] = A[c_i][j - 1]
    # 아래
    for j in range(c_i + 1, R - 1):
        A[j][0] = A[j + 1][0]
    for j in range(C - 1):
        A[R - 1][j] = A[R - 1][j + 1]
    for j in range(R - 1, c_i + 1, -1):
        A[j][C - 1] = A[j - 1][C - 1]
    for j in range(C - 1, 0, -1):
        A[c_i + 1][j] = A[c_i + 1][j - 1]
    A[c_i][0] = A[c_i][1] = 0
    A[c_i + 1][0] = A[c_i + 1][1] = 0
result = 0
for elem in A:
    result += sum(elem)
print(result)
