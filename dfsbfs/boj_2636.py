import sys
from collections import deque

# 세로 n, 가로 m
n, m = map(int, sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


# 공기 닫는 치즈는 2로 변경
# 방문한 곳은 3으로 변경 (방문 처리)
def bfs(x, y, cnt):
    deq = deque()

    deq.append([x, y])  # 시작점 큐에 넣기
    graph[x][y] = 3  # 방문 처리

    while deq:
        cur_x, cur_y = deq.popleft()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 2  # 공기 닫는 치즈는 2로 변경
                cnt += 1

            if graph[nx][ny] == 0:  # 이동 가능한 곳이면
                graph[nx][ny] = 3  # 방문 처리
                deq.append([nx, ny])  # 큐에 넣기

    return cnt  # 공기 닿은 치즈 개수 반환


# 가로 세로 최대 100
# 치즈가 있는지 체크하고 있으면 bfs

cheese = 0
time = 0
while True:
    temp = bfs(0, 0, 0)  # 공기 닿은 치즈 개수
    if temp > 0:
        cheese = temp
        time += 1
    else:  # bfs 결과 공기 닿은 치즈가 0개이면 종료
        print(time)
        print(cheese)
        break

    for i in range(n):
        for j in range(m):
            # 방문 처리한 곳과 녹는 치즈 0으로 변경
            if graph[i][j] == 2 or graph[i][j] == 3:
                graph[i][j] = 0