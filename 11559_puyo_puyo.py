from collections import deque
import pprint

arr = [list(input()) for _ in range(12)]


# 중력 -> 바닥이나 다른 뿌요까지 하강
# 같은 색이 4개 이상
# 4개 이상의 그룹이 겹쳐 있다면 동시에 터짐


def bfs(s_i, s_j, s_letter):
    q = deque([(s_i, s_j)])
    memo = [(s_i, s_j)]
    while q:
        x, y = q.popleft()
        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if not (0 <= nx < 12 and 0 <= ny < 6) or v[nx][ny]:
                continue
            if arr[nx][ny] == s_letter:
                v[nx][ny] = True
                q.append((nx, ny))
                memo.append((nx, ny))
    if len(memo) > 3:
        to_dots.extend(memo)


result = 0
while True:
    to_dots = []
    v = [[False] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if arr[i][j] == "." or v[i][j]:
                continue
            v[i][j] = True
            bfs(i, j, arr[i][j])
    if not to_dots:
        print(result)
        break
    result += 1
    for i, j in to_dots:
        arr[i][j] = 'Z'
    for i in range(12):
        for j in range(6):
            if j == 0 and arr[i][j] == 'Z':
                arr[i][j] = "."
            if j > 0:
                arr[i][j] = arr[i - 1][j]
                arr[i - 1][j] = '.'
