import sys

# 세로 M, 가로 N
M, N = map(int, sys.stdin.readline().split())

graph = []
for i in range(M):
    graph.append(list(map(int, sys.stdin.readline().split())))

dp = [[-1 for j in range(N)] for i in range(M)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    if (x == M - 1) and (y == N - 1):
        return 1

    if dp[x][y] >= 0:
        return dp[x][y]

    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= M or ny >= N:
            continue

        if graph[x][y] > graph[nx][ny]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]


print(dfs(0, 0))