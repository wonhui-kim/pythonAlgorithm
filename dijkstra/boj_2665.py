import sys
import heapq

n = int(sys.stdin.readline())
graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

INF = int(10e9)
dist = [[INF for j in range(n)] for i in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 0이 벽임
def wall(arr, x, y):
    if arr[x][y] == 0:
        return 1
    else:
        return 0


def dijkstra(x, y):
    pq = []
    dist[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue

        heapq.heappush(pq, [wall(graph, nx, ny), nx, ny])

    while pq:
        d, cur_x, cur_y = heapq.heappop(pq)

        if dist[cur_x][cur_y] != INF:
            continue

        dist[cur_x][cur_y] = d

        if cur_x == n - 1 and cur_y == n - 1:
            return

        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]

            if next_x < 0 or next_y < 0 or next_x >= n or next_y >= n:
                continue

            if dist[next_x][next_y] == INF:
                heapq.heappush(pq, [d + wall(graph, next_x, next_y), next_x, next_y])


dijkstra(0, 0)
print(dist[n - 1][n - 1])