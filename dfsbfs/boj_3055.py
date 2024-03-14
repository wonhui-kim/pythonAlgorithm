import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
graph = []
# 시작 위치, 도착 위치
start = [0, 0]
end = [0, 0]
for i in range(R):
    temp = list(sys.stdin.readline().rstrip())

    graph.append(temp)

    for j in range(len(temp)):
        if temp[j] == "D":
            end = [i, j]
        if temp[j] == "S":
            start = [i, j]

INF = int(10e9)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def water(arr):
    # 현재 물 위치들 저장
    cur_water = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == "*":
                cur_water.append([i, j])

    water_time = [[INF for i in range(C)] for j in range(R)]

    deq = deque()
    for c in cur_water:
        deq.append([c[0], c[1], 0])  # x, y, 시간 저장
        water_time[c[0]][c[1]] = 0  # 시간 저장 및 방문 처리

    while deq:
        cur_x, cur_y, time = deq.popleft()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                continue

            if graph[nx][ny] == "." and water_time[nx][ny] == INF:
                deq.append([nx, ny, time + 1])
                water_time[nx][ny] = time + 1

    return water_time


# print(water(graph))

def move(start, water_time):
    move_time = [[INF for i in range(C)] for j in range(R)]

    deq = deque()
    deq.append([start[0], start[1], 0])
    move_time[start[0]][start[1]] = 0

    while deq:
        cur_x, cur_y, time = deq.popleft()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                continue

            # 비어있으면서, 방문 안했으면서, 물이 도달하기 전에
            if (graph[nx][ny] == ".") and (move_time[nx][ny] == INF) and (water_time[nx][ny] > time + 1):
                deq.append([nx, ny, time + 1])
                move_time[nx][ny] = time + 1

    return move_time


water_time = water(graph)
move_time = move(start, water_time)

# 도착지 기준으로 4방 돌면서 min+1이 해답
result = INF
for i in range(4):
    nx = end[0] + dx[i]
    ny = end[1] + dy[i]

    if nx < 0 or ny < 0 or nx >= R or ny >= C:
        continue

    result = min(result, move_time[nx][ny])

if result >= INF:
    print("KAKTUS")
else:
    print(result + 1)