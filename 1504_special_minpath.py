from heapq import heappush, heappop

INF = int(1e10)


def dijkstra(start, end):
    visited = set()
    pq = [(0, start)]
    while pq:
        w, v = heappop(pq)
        if v == end:
            return w
        if v in visited: continue
        visited.add(v)
        for nw, nv in graph[v]:
            if nv in visited: continue
            heappush(pq, (w + nw, nv))
    return INF


N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])
v1, v2 = map(int, input().split())

d_v1 = dijkstra(1, v1)
d_v2 = dijkstra(1, v2)
d_v1_v2 = dijkstra(v1, v2)
d_v1_n = dijkstra(v1, N)
d_v2_n = dijkstra(v2, N)

d_1 = d_v1 + d_v1_v2 + d_v2_n
d_2 = d_v2 + d_v1_v2 + d_v1_n
result = min(d_1, d_2)
if result >= INF:
    print(-1)
else:
    print(result)
