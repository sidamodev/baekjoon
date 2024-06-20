N, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(2 ** N)]
L = list(map(int, input().split()))

for level in L:
    size = (2 ** N) ** 2 // (2 ** level) ** 2

