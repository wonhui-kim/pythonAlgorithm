import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())

graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))


def get_value(d):
    result = int(10e9)

    for k in range(K + 1):
        result = min(result, d[k][N - 1][M - 1])

    return result


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
INF = int(10e9)
dist = [[[INF for i in range(M)] for j in range(N)] for k in range(K + 1)]


def bfs(x, y):
    deq = deque()
    deq.append([x, y, 0])  # 벽 부순 개수 추가
    dist[0][x][y] = 1  # 처음 칸도 거리 포함

    while deq:
        cur_x, cur_y, crashed = deq.popleft()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if dist[crashed][nx][ny] < INF:
                continue

            if graph[nx][ny] == 0:  # 다음 칸이 벽이 아닐 때
                deq.append([nx, ny, crashed])
                dist[crashed][nx][ny] = dist[crashed][cur_x][cur_y] + 1
            else:  # 다음 칸이 벽일 때
                if crashed + 1 > K:  # 깰 수 있는 벽 개수 초과일 때
                    continue
                deq.append([nx, ny, crashed + 1])
                dist[crashed + 1][nx][ny] = dist[crashed][cur_x][cur_y] + 1

    return get_value(dist)


print(bfs(0, 0))