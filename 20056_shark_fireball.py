N, M, K = map(int, input().split())
d_rc = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
nd = [(0, 2, 4, 6), (1, 3, 5, 7)]
A = [[[] for __ in range(N)] for _ in range(N)]
fireball = []

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireball.append((r - 1, c - 1, m, s, d))

for _ in range(K):
    while fireball:
        r, c, m, s, d = fireball.pop()
        nr = (r + d_rc[d][0] * s) % N
        nc = (c + d_rc[d][1] * s) % N
        A[nr][nc].append([m, s, d])

    for r in range(N):
        for c in range(N):
            if not A[r][c]: continue
            len_A = len(A[r][c])
            if len_A < 2:
                fireball.append((r, c, *A[r][c].pop()))
                continue
            sum_m = sum_s = sum_d = 0
            pre_d = A[r][c][0][2] % 2
            while A[r][c]:
                m, s, d = A[r][c].pop()
                sum_m += m
                sum_s += s
                if d % 2 != pre_d:
                    sum_d = 1
                pre_d = d % 2
            nm = sum_m // 5
            ns = sum_s // len_A
            if nm == 0: continue
            for k in range(4):
                fireball.append((r, c, nm, ns, nd[sum_d][k]))

print(sum([x[2] for x in fireball]))
