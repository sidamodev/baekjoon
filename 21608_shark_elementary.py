from heapq import heappush, heappop

N = int(input())
A = [list(map(int, input().split())) for _ in range(N * N)]
C = [[0] * N for _ in range(N)]
students_dict = {}

for student, *friends in A:
    students_dict[student] = friends
    pq = []
    for i in range(N):
        for j in range(N):
            if C[i][j] != 0: continue
            friends_cnt = blank_cnt = 0
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if not (0 <= ni < N and 0 <= nj < N): continue
                if C[ni][nj] in friends:
                    friends_cnt += 1
                elif C[ni][nj] == 0:
                    blank_cnt += 1
            heappush(pq, (-friends_cnt, -blank_cnt, i, j))
    if pq:
        f, b, s_i, s_j = heappop(pq)
        C[s_i][s_j] = student

result = 0
for i in range(N):
    for j in range(N):
        like_cnt = 0
        for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if not (0 <= ni < N and 0 <= nj < N): continue
            if C[ni][nj] in students_dict[C[i][j]]:
                like_cnt += 1
        result += {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}[like_cnt]

print(result)
