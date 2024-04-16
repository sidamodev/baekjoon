N, M = map(int, input().split())
r, c, d = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
d_ij = ((-1, 0), (0, 1), (1, 0), (0, -1))


def solve():
    stk = [(r, c, d)]
    cnt = 0
    while stk:
        i, j, w = stk.pop()
        if A[i][j] == 0:
            A[i][j] = 2
            cnt += 1
        for di, dj in d_ij:
            ni, nj = i + di, j + dj
            if not (0 <= ni < N and 0 <= nj < M): continue
            if A[ni][nj] == 0:
                w = (w - 1) % 4
                ni, nj = i + d_ij[w][0], j + d_ij[w][1]
                if (0 <= ni < N and 0 <= nj < M) and A[ni][nj] == 0:
                    i, j = ni, nj
                stk.append((i, j, w))
                break
        else:  # 청소되지 않은 칸이 없는 경우
            ni, nj = i - d_ij[w][0], j - d_ij[w][1]
            if (0 <= ni < N and 0 <= nj < M) and A[ni][nj] == 2:
                stk.append((ni, nj, w))
            else:
                return cnt


print(solve())
