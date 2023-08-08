import sys
import heapq

# 정점의 개수 N, 간선 개수 E
N, E = map(int, sys.stdin.readline().split())

graph = [[] for i in range(N + 1)]
for i in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([c, b])  # 가중치, 도착노드 저장
    graph[b].append([c, a])  # 양방향이므로 양쪽 모두 저장

# 거쳐야 하는 정점 2개
v1, v2 = map(int, sys.stdin.readline().split())

# 시작 노드로부터 v1까지 거리, v2까지의 거리 구해야 함
# v1 노드로부터 v2까지의 거리, N까지의 거리 구해야 함
# v2 노드로부터 v1까지의 거리, N까지의 거리 구해야 함
INF = int(10e9)
original_dist = [INF] * (N + 1)
v1_dist = [INF] * (N + 1)
v2_dist = [INF] * (N + 1)


def dijkstra(start, dist):
    pq = []
    dist[start] = 0  # 시작노드 - 시작노드까지 거리는 0

    for v in graph[start]:
        heapq.heappush(pq, [v[0], v[1]])  # 가중치, 노드 삽입

    while pq:
        d, cur = heapq.heappop(pq)

        if dist[cur] != INF:  # 갱신된 적 있으면 넘어감
            continue

        dist[cur] = d  # 없으면 가중치로 최단거리 갱신

        for v in graph[cur]:
            if dist[v[1]] == INF:  # 갱신된 적 없는 경우
                heapq.heappush(pq, [d + v[0], v[1]])  # 시작-현재-연결노드 거리 삽입


dijkstra(1, original_dist)
dijkstra(v1, v1_dist)
dijkstra(v2, v2_dist)

# 1 -> v1 -> v2 -> N vs. 1 -> v2 -> v1 -> N
v1_first = original_dist[v1] + v1_dist[v2] + v2_dist[N]
v2_first = original_dist[v2] + v2_dist[v1] + v1_dist[N]

result = min(v1_first, v2_first)
if result >= INF:  # 연결 경로가 없으면 INF 가 더해져 INF보다 큰 수가 나옴
    print(-1)
else:
    print(result)