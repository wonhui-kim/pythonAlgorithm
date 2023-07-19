import sys

#동전 종류 n, 가치 합 k
n, k = map(int, sys.stdin.readline().split())

#각 동전 가치 저장
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))

dp = [0 for i in range(k+1)] #dp 0으로 초기화
for c in coins: #<=100
    for w in range(c, k+1): #<=10,000
        if c == w:
            dp[w] += 1
        else:
            dp[w] += dp[w-c]

print(dp[k])