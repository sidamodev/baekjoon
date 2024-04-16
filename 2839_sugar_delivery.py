N = int(input())
memo = [0] * (N * 3)


def dp(n):
    for i in range(3, n + 1):
        if i % 5 == 0:
            memo[i] = memo[i - 5] + 1
        elif i % 3 == 0:
            memo[i] = memo[i - 3] + 1
        else:
            memo[i] = min(memo[i - 3] + 1, memo[i - 5] + 1)
    return memo[n]


if N == 4 or N == 7:
    print(-1)
else:
    print(dp(N))
