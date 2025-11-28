from collections import deque

N, K = map(int, input().split())

q = deque([N])
visited = [0] * 1000001
while q:
    current = q.popleft()
    if current == K:
        print(visited[current])
        break
    for fun in [lambda x: x - 1, lambda x: x + 1, lambda x: 2 * x]:
        if 0 <= fun(current) <= 1000000 and not visited[fun(current)]:
            visited[fun(current)] = visited[current] + 1
            q.append(fun(current))
