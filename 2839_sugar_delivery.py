N = int(input())
memo = [0] * (N * 3)


def dp(i):
    if i <= 3 or i == 5:
        return 1
    elif memo[i]:
        return memo[i]
    else:
        memo[i] = min(dp(i - 3) + 1, dp(i - 5) + 1)
        return memo[i]


if N == 4 or N == 7:
    print(-1)
else:
    print(dp(N))
