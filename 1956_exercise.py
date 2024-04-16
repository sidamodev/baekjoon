from heapq import heappush, heappop

V, E = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(E)]

# prim

