import sys

#퇴사일까지 남은 날짜
N = int(sys.stdin.readline())

T = [0]
P = [0]
for i in range(N):
    t, p = map(int, sys.stdin.readline().split())
    T.append(t)
    P.append(p)

dp = [0 for i in range(N+2)]
for i in range(N, 0, -1):
    if T[i]+i <= N+1:
        dp[i] = max(P[i] + dp[i+T[i]], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[1])