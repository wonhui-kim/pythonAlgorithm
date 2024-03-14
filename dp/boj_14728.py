import sys

N, T = map(int, sys.stdin.readline().split())
time = []
score = []

for i in range(N):
    K, S = map(int, sys.stdin.readline().split())
    time.append(K)
    score.append(S)

dp = [[0 for i in range(T+1)] for j in range(N)]
for i in range(N):
    for j in range(T+1):
        if j >= time[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-time[i]] + score[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N-1][T])