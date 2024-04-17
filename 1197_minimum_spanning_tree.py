from heapq import heappush, heappop

V, E = map(int, input().split())
adj = [[] for _ in range(V + 1)]

for _ in range(E):
    A, B, C = map(int, input().split())
    adj[A].append((B, C))
    adj[B].append((A, C))
init_node = [[i][0][0][0] for i in adj if i][0]
pq = [(0, init_node)]
mst = set()
total_w = 0
while len(mst) < V:
    w, n = heappop(pq)
    if n in mst: continue
    mst.add(n)
    total_w += w
    for nv, nw in adj[n]:
        if nv in mst: continue
        heappush(pq, (nw, nv))

print(total_w)
