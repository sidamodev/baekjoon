import queue

N, M = map(int, input().split())
ladder = [list(map(int, input().split())) for _ in range(N)]
snake = [list(map(int, input().split())) for _ in range(M)]
board = [0 for _ in range(101)]

for x, y in ladder:
    board[x] = y

for u, v in snake:
    board[u] = v

q = queue.Queue()
q.put(1)
visit = [0] * 101
visit[1] = 1
while not q.empty():
    pos = q.get()
    if pos == 100: break
    for i in range(1, 7):
        if pos + i > 100: continue
        next_pos = board[pos + i]
        if not next_pos:
            next_pos = pos + i
        if visit[next_pos]: continue
        visit[next_pos] = visit[pos] + 1
        q.put(next_pos)

print(visit[100] - 1)
