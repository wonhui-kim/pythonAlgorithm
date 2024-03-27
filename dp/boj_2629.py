import sys

N = int(sys.stdin.readline())
weight = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
ball = list(map(int, sys.stdin.readline().split()))

dp = [[0 for i in range(40001)] for j in range(N + 1)]


def backtracking(n, w):  # 추 번호와 만드는 무게
    if n > N:  # 추 인덱스 아웃
        return

    if w < 0:
        return

    if dp[n][w] == 1:
        return

    dp[n][w] = 1

    backtracking(n + 1, w + weight[n - 1])
    backtracking(n + 1, w)
    backtracking(n + 1, abs(w - weight[n - 1]))


backtracking(0, 0)

for b in ball:
    if dp[N][b] == 1:
        print("Y", end=' ')
    else:
        print("N", end=' ')