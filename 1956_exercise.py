from heapq import heappush, heappop


def dijkstra(start_v):
    visit = set()
    pq = [(0, start_v)]
    w_acc = 0
    while pq:
        w, v = heappop(pq)
        w_acc += w
        if w and v == start_v: return w_acc
        if v in visit: break
        visit.add(v)
        for nv, nw in adj[v]:
            heappush(pq, (nw, nv))


V, E = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(E)]
adj = [[] for _ in range(V + 1)]

for s, e, w in g:
    adj[s].append((e, w))

dist_lst = []
for i in range(1, V + 1):
    if not adj[i]: continue
    tmp = dijkstra(i)
    if tmp: heappush(dist_lst, tmp)

result = -1
if dist_lst:
    result = heappop(dist_lst)
print(result)
