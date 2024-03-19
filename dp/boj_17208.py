import sys

N, M, K = map(int, sys.stdin.readline().split())

burgers = []
fries = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())

    burgers.append(x)
    fries.append(y)

dp = [[[0 for i in range(K + 1)] for j in range(M + 1)] for k in range(N)]

for i in range(N):  # 주문 수
    for j in range(M + 1):  # 치즈버거
        for k in range(K + 1):  # 감자튀김
            if (j >= burgers[i]) and (k >= fries[i]):
                dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - burgers[i]][k - fries[i]] + 1)
            else:
                dp[i][j][k] = dp[i - 1][j][k]

print(dp[N - 1][M][K])