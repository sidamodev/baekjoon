N = int(input())

min_cnt = 0xFFFF


def solve(n, X):
    global min_cnt
    if n >= min_cnt:
        return
    if X == 1:
        if n < min_cnt:
            min_cnt = n
        return

    if X % 3 == 0:
        solve(n + 1, X / 3)
    if X % 2 == 0:
        solve(n + 1, X / 2)
    solve(n + 1, X - 1)


solve(0, N)
print(min_cnt)
