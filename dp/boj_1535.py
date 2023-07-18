import sys

#사람 수 N
N = int(sys.stdin.readline())

#체력
L = list(map(int, sys.stdin.readline().split()))

#기쁨
J = list(map(int, sys.stdin.readline().split()))

#dp 배열 초기화 -> 최대 기쁨 저장
dp = [[0 for j in range(101)] for i in range(N+1)]

for k in range(N+1): #0~N
    for l in range(101): #0~100(체력)
        if k == 0 or l == 0:
            dp[k][l] = 0
        elif l > L[k-1]: #체력이 0이거나 음수가 되면 죽음
            dp[k][l] = max(dp[k-1][l], dp[k-1][l-L[k-1]]+J[k-1])
        else:
            dp[k][l] = dp[k-1][l]

print(dp[N][100])