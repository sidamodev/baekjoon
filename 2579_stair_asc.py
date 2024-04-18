N = int(input())
A = [0] + [int(input()) for _ in range(N)]

memo = [0] * (N + 1)
memo[1] = A[1]
memo[2] = A[2]
memo[3] = A[1] + A[2]


def dp(i, c):
    if i < 3:
        return A[i]
    elif memo[i]:
        return memo[i]
    else:
        if c == 2:
            memo[i] = dp(i - 2, 1) + A[i]
        else:
            memo[i] = max(dp(i - 2, 1) + A[i], dp(i - 1, c + 1) + A[i])
        return memo[i]


dp(N, 1)
print(memo[N])
