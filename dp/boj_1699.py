import sys
import math

N = int(sys.stdin.readline())

dp = list(range(N + 1))  # [0, 1, 2, 3, 4, 5, 6, ..., N] 으로 초기화
for i in range(1, len(dp)):
    if int(math.sqrt(dp[i])) ** 2 == dp[i]:  # 제곱수인지 판별
        dp[i] = 1

# 수 k는 N의 제곱근만큼만 돌면된다.
for k in range(2, int(math.sqrt(N) + 1)):
    for w in range(k ** 2, N + 1):
        if dp[w] > dp[w - (k ** 2)] + 1:
            dp[w] = dp[w - (k ** 2)] + 1

print(dp[N])