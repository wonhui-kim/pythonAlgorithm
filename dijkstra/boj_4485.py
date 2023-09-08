import sys
import heapq

order = 1
while True:
    N = int(sys.stdin.readline())

    if N == 0:
        break

    cave = []
    for i in range(N):
        cave.append(list(map(int, sys.stdin.readline().split())))

    INF = int(10e9)
    dist = [[INF for j in range(N)] for i in range(N)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]


    def dijkstra(x, y):
        pq = []
        dist[x][y] = cave[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            # 시작점 가중치 + 현재 가중치
            heapq.heappush(pq, [dist[x][y] + cave[nx][ny], nx, ny])

        while pq:
            cur_d, cur_x, cur_y = heapq.heappop(pq)

            # 이미 갱신된 적 있으면 continue
            if dist[cur_x][cur_y] != INF:
                continue

            # 갱신되지 않았다면 갱신해줌
            dist[cur_x][cur_y] = cur_d

            for i in range(4):
                nx = cur_x + dx[i]
                ny = cur_y + dy[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue

                if dist[nx][ny] == INF:
                    heapq.heappush(pq, [cur_d + cave[nx][ny], nx, ny])


    dijkstra(0, 0)
    print("Problem " + str(order) + ": " + str(dist[N - 1][N - 1]))
    order += 1