import sys
import heapq

M, N = map(int, sys.stdin.readline().split())
graph = []

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

INF = int(10e9)
dist = [[INF for j in range(M)] for i in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dijkstra(x, y):
    pq = []
    dist[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue

        # 가중치, x, y 좌표
        heapq.heappush(pq, [graph[nx][ny], nx, ny])

    while pq:
        d, cur_x, cur_y = heapq.heappop(pq)

        if dist[cur_x][cur_y] != INF:
            continue

        dist[cur_x][cur_y] = d

        if cur_x == N - 1 and cur_y == M - 1:
            return

        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]

            if next_x < 0 or next_y < 0 or next_x >= N or next_y >= M:
                continue

            if dist[next_x][next_y] == INF:
                heapq.heappush(pq, [d + graph[next_x][next_y], next_x, next_y])


dijkstra(0, 0)
print(dist[N - 1][M - 1])