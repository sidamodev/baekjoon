import pprint

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

T = [N // 2, N // 2]  # 토네이도 시작점
d_ij = ((0, -1), (1, 0), (0, 1), (-1, 0))
result = 0

mask = [[0, 0, 2, 0, 0],
        [0, 10, 7, 1, 0],
        [5, 0, 0, 0, 0],
        [0, 10, 7, 1, 0],
        [0, 0, 2, 0, 0]]


def rotate_mask():
    global mask
    new_mask = [[0] * 5 for _ in range(5)]
    for r in range(5):
        for c in range(5):
            new_mask[5 - c - 1][r] = mask[r][c]
    mask = [x[:] for x in new_mask]


def tornado(r, c):
    if A[r][c] == 0: return 0
    out_sand = 0
    y = a = A[r][c]
    A[r][c] = 0
    for p in range(5):
        for q in range(5):
            if mask[p][q] == 0: continue
            n_sand = (y * mask[p][q]) // 100
            a -= n_sand
            nr, nc = r + p - 2, c + q - 2  # 실좌표
            if 0 <= nr < N and 0 <= nc < N:  # 좌표 내부라면 반영
                A[nr][nc] += n_sand
            else:
                out_sand += n_sand
    nr = r + d_ij[d][0]
    nc = c + d_ij[d][1]
    if 0 <= nr < N and 0 <= nc < N:
        A[nr][nc] += a
    else:
        out_sand += a
    return out_sand


# 좌 하 우 상
# 1 1 2 2 3 3 4 4 5 5 6 6 7 -> 규칙
d = prev_d = 0
for i in range(1, N + 1):
    for j in range(2):
        for k in range(i):
            # 로직 실행하고 좌표 증가
            T[0] += d_ij[d][0]
            T[1] += d_ij[d][1]
            result += tornado(T[0], T[1])
        d = (d + 1) % 4
        rotate_mask()
        if i == N: break
print(result)
