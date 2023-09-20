import sys
import heapq

tc = int(sys.stdin.readline())

for t in range(tc):
    # 컴퓨터 개수 n, 의존성 개수 d, 해킹 컴퓨터 c(시작점)
    n, d, c = map(int, sys.stdin.readline().split())

    graph = [[] for i in range(n + 1)]
    for i in range(d):
        a, b, s = map(int, sys.stdin.readline().split())

        graph[b].append([s, a])  # b -> a 해킹이므로

    INF = int(10e9)
    dist = [INF for i in range(n + 1)]


    def dijkstra(start):
        pq = []
        dist[start] = 0  # 본인은 0

        for v in graph[start]:
            heapq.heappush(pq, v)

        while pq:
            d, cur = heapq.heappop(pq)

            if dist[cur] != INF:  # 이미 갱신된 적 있으면
                continue

            dist[cur] = d

            for v in graph[cur]:
                heapq.heappush(pq, [d + v[0], v[1]])


    dijkstra(c)

    cnt = 0
    time = 0
    for d in dist:
        if d < INF:
            cnt += 1
            time = max(d, time)  # 마지막 컴퓨터 감염까지의 시간

    print(cnt, time)