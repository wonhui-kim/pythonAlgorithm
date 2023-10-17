import sys

# 테스트케이스 수
T = int(sys.stdin.readline())

dp = [[0, 0, 0] for i in range(100001)]

# 초기 값(각 1, 2, 3으로 끝나는 개수)
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for j in range(4, 100001):
    dp[j][0] = dp[j - 1][1] % 1000000009 + dp[j - 1][2] % 1000000009
    dp[j][1] = dp[j - 2][0] % 1000000009 + dp[j - 2][2] % 1000000009
    dp[j][2] = dp[j - 3][0] % 1000000009 + dp[j - 3][1] % 1000000009

for i in range(T):
    n = int(sys.stdin.readline())

    if n == 0:
        print(0)
        continue
    elif n == 1 or n == 2:
        print(1)
        continue
    elif n == 3:
        print(3)
        continue
    else:
        print(sum(dp[n]) % 1000000009)