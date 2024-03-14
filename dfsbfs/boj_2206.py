import sys
from collections import deque
import copy

N, M = map(int, sys.stdin.readline().split())

graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

INF = int(10e9)


def bfs(x, y, arr):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 방문 처리 및 최단거리 저장
    dist = [[[INF for i in range(2)] for j in range(M)] for k in range(N)]
    dist[x][y][0] = 1  # 문제에서 시작칸도 포함한다 했음

    deq = deque()
    deq.append([x, y, 0])  # 마지막 원소는 벽을 부쉈는지 아닌지 여부

    while deq:
        cur_x, cur_y, crashed = deq.popleft()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            # 이미 갱신한 곳이면 skip
            if dist[nx][ny][crashed] != INF:
                continue

            if arr[nx][ny] == 0:  # 이동할 수 있는 곳이면
                deq.append([nx, ny, crashed])
                dist[nx][ny][crashed] = dist[cur_x][cur_y][crashed] + 1
            else:  # arr[nx][ny] == 1 이동할 수 없는 곳이면
                if crashed >= 1:  # 이미 벽 부쉈으면
                    continue
                deq.append([nx, ny, crashed + 1])  # 벽부수고 감
                dist[nx][ny][crashed + 1] = dist[cur_x][cur_y][crashed] + 1

    return min(dist[N - 1][M - 1])


result = bfs(0, 0, graph)

if result >= INF:
    result = -1

print(result)