import sys
import heapq

n, m = map(int, sys.stdin.readline().split())

INF = int(10e9)
graph = [[] for i in range(n + 1)]
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())

    # [가중치, 연결노드] 추가
    graph[a].append([c, b])
    graph[b].append([c, a])

s, t = map(int, sys.stdin.readline().split())

dist = [INF] * (n + 1)


def dijkstra(start):
    pq = []
    dist[start] = 0  # 시작점으로까지의 거리는 0

    for v in graph[start]:
        heapq.heappush(pq, [v[0], v[1]])

    while pq:
        d, cur = heapq.heappop(pq)

        # 갱신된 적이 있으면 스킵
        if dist[cur] != INF:
            continue

        # 현재 노드 갱신
        dist[cur] = d

        for v in graph[cur]:
            if dist[v[1]] == INF:
                heapq.heappush(pq, [v[0] + d, v[1]])


# 시작점 s 으로부터 다익스트라(최단거리 구하기)
dijkstra(s)
print(dist[t])
