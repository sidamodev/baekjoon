from heapq import heappush, heappop

R, C, K = map(int, input().split())
R -= 1
C -= 1
len_r = len_c = 3
time = 0

A = [list(map(int, input().split())) for _ in range(3)]


def making_count_heap(cnt):  # 최소힙으로 수, 수의 개수 순 정렬
    heap = []
    for k, item in enumerate(cnt):
        if k == 0: continue
        if item > 0:
            heappush(heap, (item, k))
    return heap


def sorted_array(heap):
    sorted_arr = []
    while heap:
        item, idx = heappop(heap)
        sorted_arr.append(idx)
        sorted_arr.append(item)
    return sorted_arr


def sort_array_and_calc_len(len_r, len_c, A):
    tmp_len_c = 0
    for i in range(len_r):
        cnt = [0] * 101
        for j in range(len_c):
            if A[i][j] > 0:
                cnt[A[i][j]] += 1
        heap = making_count_heap(cnt)
        A[i] = sorted_array(heap)
        if tmp_len_c < len(A[i]):
            tmp_len_c = len(A[i])
    return tmp_len_c


def insert_padding_zero(A, len_r, len_c):
    for i in range(len_r):
        if len(A[i]) < len_c:
            A[i] += [0] * (len_c - len(A[i]))


for time in range(101):
    if not (len_r <= R or len_c <= C) and A[R][C] == K: break
    if len_r >= len_c:
        len_c = sort_array_and_calc_len(len_r, len_c, A)
        insert_padding_zero(A, len_r, len_c)
    else:
        A = [list(elem) for elem in zip(*A)]  # 전치행렬
        len_r = sort_array_and_calc_len(len_c, len_r, A)
        insert_padding_zero(A, len_c, len_r)
        A = [list(elem) for elem in zip(*A)]  # 전치행렬의 전치행렬 -> 원래 행렬
else:
    time = -1
print(time)
