import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
opr = list(map(int, input().split()))
min_v, max_v = 1e9, -1e9


def solve(lev, sum_v):
    global min_v, max_v
    if lev == N:
        max_v = max(max_v, sum_v)
        min_v = min(min_v, sum_v)
        return
    if opr[0] > 0:
        opr[0] -= 1
        solve(lev + 1, sum_v + A[lev])
        opr[0] += 1
    if opr[1] > 0:
        opr[1] -= 1
        solve(lev + 1, sum_v - A[lev])
        opr[1] += 1
    if opr[2] > 0:
        opr[2] -= 1
        solve(lev + 1, sum_v * A[lev])
        opr[2] += 1 
    if opr[3] > 0:
        opr[3] -= 1
        solve(lev + 1, int(sum_v / A[lev]))
        opr[3] += 1


solve(1, A[0])
print( int(max_v), int(min_v), sep="\n")


