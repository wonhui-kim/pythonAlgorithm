import sys
import heapq

while True:
    # 장소 수(정점), 도로 수(간선)
    N, M = map(int, sys.stdin.readline().split())

    if N == 0 and M == 0:  # 종료 조건
        break

    # 시작점, 도착점
    S, D = map(int, sys.stdin.readline().split())

    graph = [[] for i in range(N)]  # 0번부터 N-1번
    reverse_graph = [[] for i in range(N)]  # 역방향 그래프 저장
    for i in range(M):
        U, V, P = map(int, sys.stdin.readline().split())
        graph[U].append([P, V])
        reverse_graph[V].append([P, U])

    # 최단 경로에 들어가는 길인지 체크
    check_way = [([False] * N) for i in range(N)]

    INF = int(10e9)
    dist = [INF] * N


    def dijkstra(start):
        pq = []
        dist[start] = 0

        for v in graph[start]:
            if not check_way[start][v[1]]:  # 최단경로에 들어가는 경로가 아닐 때만
                heapq.heappush(pq, [v[0], v[1]])

        while pq:
            w, cur = heapq.heappop(pq)

            if dist[cur] != INF:
                continue

            dist[cur] = w

            for v in graph[cur]:
                if dist[v[1]] == INF and not check_way[cur][v[1]]:
                    heapq.heappush(pq, [w + v[0], v[1]])


    dijkstra(S)


    def find_way(start):
        pq = []

        for v in reverse_graph[start]:
            if dist[start] == v[0] + dist[v[1]]:
                check_way[v[1]][start] = True
                heapq.heappush(pq, [v[0], v[1]])

        while pq:
            w, cur = heapq.heappop(pq)

            if cur == 0:  # 시작점이면
                continue  # break 안하는 이유는 길이 여러개일 수 있기에

            for past_dist, past in reverse_graph[cur]:
                if check_way[past][cur]:  # 이미 최단경로 체크
                    continue
                if dist[cur] == dist[past] + past_dist:
                    check_way[past][cur] = True
                    heapq.heappush(pq, [w + past_dist, past])


    find_way(D)  # 최단경로에 들어가는 경로를 찾음

    dist = [INF] * N  # dist 다시 초기화
    dijkstra(S)

    if dist[D] >= INF:
        print(-1)
    else:
        print(dist[D])