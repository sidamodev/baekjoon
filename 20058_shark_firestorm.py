N, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(2 ** N)]
L = list(map(int, input().split()))

for level in L:
    total_grid = (2 ** N) ** 2
    sub_grid = (2 ** level) ** 2
    sub_total = total_grid // sub_grid
    # sub_line = int(sub_total ** 0.5)
    for i in range(sub_total):
        print(i, i//sub_)
