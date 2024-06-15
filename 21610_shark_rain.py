def input_list():
    return map(int, input().split())


N, M = input_list()
A = [list(input_list()) for _ in range(N)]
move = [list(input_list()) for _ in range(M)]

d_ij = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
cloud = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

for d, s in move:
    prev_cloud = set()
    for cloud_i, cloud_j in cloud:
        ni = (cloud_i + d_ij[d - 1][0] * s) % N
        nj = (cloud_j + d_ij[d - 1][1] * s) % N
        A[ni][nj] += 1
        prev_cloud.add((ni, nj))
    cloud = []
    for i, j in prev_cloud:
        diag_sum = 0
        for ni, nj in [(i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1)]:
            if not (0 <= ni < N and 0 <= nj < N): continue
            if A[ni][nj]:
                diag_sum += 1
        A[i][j] += diag_sum
    for i in range(N):
        for j in range(N):
            if A[i][j] >= 2 and (i, j) not in prev_cloud:
                A[i][j] -= 2
                cloud.append((i, j))

print(sum(map(sum, A)))
