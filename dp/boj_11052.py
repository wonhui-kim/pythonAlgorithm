import sys

N = int(sys.stdin.readline())

# 1번 카드팩 가격 -> P[0]
P = list(map(int, sys.stdin.readline().split()))

dp = [0 for i in range(N + 1)]  # dp[0] = 0

for i in range(1, N + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + P[j - 1])

print(dp[N])