import sys

N, M = map(int, sys.stdin.readline().split())

D = [0] #일 수
P = [0] #페이지 수

for i in range(M):
    d, p = map(int, sys.stdin.readline().split())
    D.append(d)
    P.append(p)

dp = [[0 for i in range(N+1)] for j in range(M+1)]

for n in range(1, M+1):
    for w in range(N+1):
        if w >= D[n]:
            dp[n][w] = max(dp[n-1][w], dp[n-1][w-D[n]]+P[n])
        else:
            dp[n][w] = dp[n-1][w]

print(dp[M][N])