import sys

N, K = map(int, sys.stdin.readline().split())

importance = [0]
time = [0]
for i in range(K):
    l, t = map(int, sys.stdin.readline().split())
    importance.append(l)
    time.append(t)

dp = [[0 for i in range(N+1)] for j in range(K+1)]

for i in range(1, K+1):
    for j in range(N+1):
        if j >= time[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-time[i]] + importance[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[K][N])