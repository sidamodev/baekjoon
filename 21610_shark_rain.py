def input_list():
    return map(int, input().split())


N, M = input_list()
A = [list(input_list()) for _ in range(N)]
move = [list(input_list()) for _ in range(M)]


class Cloud:
    move_arr = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

    def __init__(self):
        self.cloud = [[0] * N for _ in range(N)]
        self.cloud[N - 1][0] = 1
        self.cloud[N - 1][1] = 1
        self.cloud[N - 2][0] = 1
        self.cloud[N - 2][1] = 1

    def move(self, direction, dist):
        tmp_arr = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if self.cloud[i][j] == 0: continue
                ni, nj = i, j
                for k in range(dist):
                    ni, nj = ni + Cloud.move_arr[direction - 1][0], nj + Cloud.move_arr[direction - 1][1]
                    if ni < 0:
                        ni = N - 1
                    elif ni >= N:
                        ni = 0
                    if nj < 0:
                        nj = N - 1
                    elif nj >= N:
                        nj = 0
                tmp_arr[ni][nj] = 1
        self.cloud = [x[:] for x in tmp_arr]

    def make(self, rained):
        for i in range(N):
            for j in range(N):
                if A[i][j] >= 2 and (i, j) not in rained:
                    A[i][j] -= 2
                    self.cloud[i][j] = 1

    def remove(self):
        self.cloud = [[0] * N for _ in range(N)]


def rain(cloud):
    rained = []
    for i in range(N):
        for j in range(N):
            if cloud[i][j]:
                rained.append((i, j))
                A[i][j] += 1
    return rained


def copy_bug(rain_arr):
    for i, j in rain_arr:
        diag_water = 0
        for ni, nj in [(i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1)]:
            if not (0 <= ni < N and 0 <= nj < N): continue
            if A[ni][nj]:
                diag_water += 1
        A[i][j] += diag_water


c = Cloud()
for d, s in move:
    c.move(d, s)
    cloud_regin = rain(c.cloud)
    c.remove()
    copy_bug(cloud_regin)
    c.make(cloud_regin)

print(sum(map(sum, A)))
