import sys


def dfs(x, y, arr):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    stack = []
    stack.append([x, y])
    arr[x][y] = 2  # 방문 처리

    while stack:
        cur_x, cur_y = stack.pop()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if nx < 0 or ny < 0 or nx >= len(arr) or ny >= len(arr[0]):
                continue

            if arr[nx][ny] == 0:
                stack.append([nx, ny])
                arr[nx][ny] = 2


M, N = map(int, sys.stdin.readline().split())
graph = []

for i in range(M):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

for i in range(N):
    if graph[0][i] == 0:
        dfs(0, i, graph)

answer = "NO"
# 가장 안쪽 검사
for i in range(N):
    if graph[M - 1][i] == 2:
        answer = "YES"

print(answer)