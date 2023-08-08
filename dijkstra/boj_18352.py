import sys
import heapq

# 도시 개수(정점), 도로 개수(간선), K, X(출발 도시)
N, M, K, X = map(int, sys.stdin.readline().split())

graph = [[] for i in range(N + 1)]
for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append([1, B])  # 가중치 1, 도착 도시

INF = int(10e9)
dist = [INF] * (N + 1)


def dijkstra(start):
    pq = []
    dist[start] = 0

    for v in graph[start]:
        heapq.heappush(pq, [v[0], v[1]])  # 가중치, 도착도시

    while pq:
        d, cur = heapq.heappop(pq)

        if dist[cur] != INF:
            continue

        dist[cur] = d

        for v in graph[cur]:
            if dist[v[1]] == INF:
                heapq.heappush(pq, [d + v[0], v[1]])


dijkstra(X)
flag = False  # 거리가 K인 것이 하나라도 있었는지 여부
for i in range(1, N + 1):
    if dist[i] == K:
        flag = True
        print(i)

if not flag:
    print(-1)
