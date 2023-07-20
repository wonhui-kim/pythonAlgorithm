import sys

N = int(sys.stdin.readline())

dp = [0 for i in range(N + 1)]

if N >= 2:
    dp[2] = 3

if N >= 4:
    for i in range(4, N + 1):
        if i % 2 == 1:  # 홀수이면 경우의 수 0
            continue

        dp[i] += (dp[i - 2] * dp[2])

        # range(start, end, step)
        for j in range(i, 3, -2):
            dp[i] += (dp[i - j] * 2)

        dp[i] += 2  # 새로운 모양 2개 추가

print(dp[N])