import sys
import heapq

# 정점 개수, 간선 개수
N, M = map(int, sys.stdin.readline().split())

# 정점이 1부터 시작하므로 개수를 N+1로 설정
graph = [[] for i in range(N + 1)]

for i in range(M):
    A, B, C = map(int, sys.stdin.readline().split())

    # 양방향 간선
    graph[A].append([C, B])  # 가중치를 0번 인덱스로 저장
    graph[B].append([C, A])

INF = int(10e9)

dist = [INF] * (N + 1)


def dijkstra(start):
    pq = []
    dist[start] = 0  # 시작점까지의 최단거리 0으로 설정

    for v in graph[start]:
        heapq.heappush(pq, v)

    while pq:
        d, cur = heapq.heappop(pq)

        # 갱신된 적 있으면 skip
        if dist[cur] != INF:
            continue

        dist[cur] = d

        for v in graph[cur]:
            if dist[v[1]] == INF:
                heapq.heappush(pq, [d + v[0], v[1]])


dijkstra(1)
print(dist[N])