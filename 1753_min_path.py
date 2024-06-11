from heapq import heappush, heappop

V, E = map(int, input().split())
K = int(input())
INF = int(1e9)

adj = [{} for _ in range(V + 1)]
dist = [INF] * (V + 1)
pq = [(0, K)]

for _ in range(E):
    u, v, w = map(int, input().split())
    if adj[u].get(v, INF) < w: continue
    adj[u][v] = w

dist[K] = 0
while pq:
    d, v = heappop(pq)
    if d > dist[v]: continue
    for nv, nd in adj[v].items():
        cost = d + nd
        if cost < dist[nv]:
            dist[nv] = cost
            heappush(pq, (d + nd, nv))

for i in range(1, V + 1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
