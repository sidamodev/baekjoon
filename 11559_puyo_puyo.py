from collections import deque

arr = [list(input()) for _ in range(12)]
print(arr)

# 중력 -> 바닥이나 다른 뿌요까지 하강
# 같은 색이 4개 이상
# 4개 이상의 그룹이 겹쳐 있다면 동시에 터짐


def bfs(s_i, s_j, s_letter):
    v = [[False] * 6 for _ in range(12)]
    q = deque(
        [
            (
                s_i,
                s_j,
            )
        ]
    )
    x, y = q.popleft()
    for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if not (0 <= x < 12 and 0 <= y < 6):
            continue
        if arr[nx][ny] == s_letter:
            q.append((nx, ny))


for i in range(12):
    for j in range(6):
        if arr[i][j] == ".":
            continue
        bfs(i, j)
