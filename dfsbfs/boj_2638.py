import sys
import copy

N, M = map(int, sys.stdin.readline().split())
graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y, arr):
    stack = []
    stack.append([x, y])
    arr[x][y] = True

    while stack:
        cur_x, cur_y = stack.pop()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if (graph[nx][ny] == 0) and (arr[nx][ny] == False):
                stack.append([nx, ny])
                arr[nx][ny] = True


# 외부 공기 판단
def check_air(arr):
    air = [[False for i in range(len(arr[0]))] for j in range(len(arr))]

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if (arr[i][j] == 0) and (not arr[i][j]):
                if i == 0 or j == 0 or i == (N - 1) or j == (M - 1):
                    dfs(i, j, air)

    return air


# 치즈 위치
def cheese_loc(arr):
    cheese = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 1:
                cheese.append([i, j])

    return cheese


# 1시간 후 치즈 상태
def melt(arr, cheese, air):
    after = copy.deepcopy(arr)

    for c in cheese:
        air_cnt = 0
        for i in range(4):
            nx = c[0] + dx[i]
            ny = c[1] + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if arr[nx][ny] == 0 and air[nx][ny]:
                air_cnt += 1

        if air_cnt >= 2:
            after[c[0]][c[1]] = 0  # 녹음

    return after


time = 0
while True:
    air = check_air(graph)  # 외부 공기 판단
    cheese = cheese_loc(graph)

    if len(cheese) == 0:
        print(time)
        break

    graph = melt(graph, cheese, air)  # 그래프 녹은 후로 변경
    time += 1  # 시간 증가