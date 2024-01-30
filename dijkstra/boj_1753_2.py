import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

graph = [[] for i in range(V + 1)]
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())

    graph[u].append([w, v])

INF = int(10e9)
dist = [INF] * (V + 1)


def dijkstra(start):
    pq = []
    dist[start] = 0  # 시작점 - 시작점까지 거리

    for v in graph[start]:
        heapq.heappush(pq, v)

    while pq:
        d, cur = heapq.heappop(pq)

        if dist[cur] != INF:  # 이미 갱신된 적 있으면
            continue

        dist[cur] = d  # 아니면 갱신

        for v in graph[cur]:
            if dist[v[1]] == INF:  # 갱신된 적 없으면
                heapq.heappush(pq, [d + v[0], v[1]])


def print_result(arr):
    for i in range(1, len(arr)):
        if arr[i] >= INF:
            print("INF")
        else:
            print(arr[i])


dijkstra(K)
print_result(dist)