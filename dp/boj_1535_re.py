import sys

#사람 수
N = int(sys.stdin.readline())

#잃는 체력
L = list(map(int, sys.stdin.readline().split()))
L.insert(0, 0)

#얻는 기쁨
J = list(map(int, sys.stdin.readline().split()))
J.insert(0, 0)

#체력은 0이되면 안되므로 0~99임
dp = [[0 for i in range(100)] for j in range(N+1)]

for n in range(1, N+1):
    for w in range(100):
        if w >= L[n]:
            dp[n][w] = max(dp[n-1][w], dp[n-1][w-L[n]] + J[n])
        else:
            dp[n][w] = dp[n-1][w]

print(dp[N][99])