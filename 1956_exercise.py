V, E = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(E)]
adj = [{} for _ in range(V + 1)]

for s, e, w in g:
    adj[s][e] = w

INF = int(1e9)
result = INF
dist = [[INF] * (V + 1) for _ in range(V + 1)]

for i in range(1, V + 1):
    for j in range(1, V + 1):
        dist[i][j] = adj[i].get(j, INF)

for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            if i == j:
                if dist[i][j] < result:
                    result = dist[i][j]
print(result if result != INF else -1)
