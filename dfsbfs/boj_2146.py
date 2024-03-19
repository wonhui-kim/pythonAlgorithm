import sys
import copy
from collections import deque

N = int(sys.stdin.readline())
graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
INF = int(10e9)


def get_bridge(x, y, arr):
    location = []

    stack = []
    stack.append([x, y])
    location.append([x, y])
    arr[x][y] = 0  # 방문 완료

    while stack:
        cur_x, cur_y = stack.pop()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if arr[nx][ny] == 1:
                stack.append([nx, ny])
                location.append([nx, ny])
                arr[nx][ny] = 0

    return location


def bfs(bridge, arr):
    dist = [[INF for i in range(N)] for j in range(N)]

    deq = deque()

    for b in bridge:
        deq.append([b[0], b[1], 0])

    while deq:
        cur_x, cur_y, d = deq.popleft()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if (dist[nx][ny] == INF) and (arr[nx][ny] == 0):
                deq.append([nx, ny, d + 1])
                dist[nx][ny] = d + 1

    return dist


def min_dist(bridge, dist, arr):
    d = INF

    for b in bridge:  # 사방만 검사
        for i in range(4):
            nx = b[0] + dx[i]
            ny = b[1] + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if arr[nx][ny] == 0:
                d = min(d, dist[nx][ny])

    return d


bridges = []
copied = copy.deepcopy(graph)
for i in range(N):
    for j in range(N):
        if copied[i][j] == 1:
            bridges.append(get_bridge(i, j, copied))

result = INF
for i in range(len(bridges) - 1):
    dist = bfs(bridges[i], graph)

    for j in range(i + 1, len(bridges)):  # 다음 섬까지 검사
        result = min(result, min_dist(bridges[j], dist, graph))

print(result)