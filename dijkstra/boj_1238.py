import sys
import heapq

# 학생(마을) 수, 도로 수, 목적 마을
N, M, X = map(int, sys.stdin.readline().split())

graph = [[] for i in range(N + 1)]
for i in range(M):
    a, b, t = map(int, sys.stdin.readline().split())
    graph[a].append([t, b])  # 소요시간, 목적 마을 저장

INF = int(10e9)

# 모든 마을에서부터 X마을까지의 최단거리가 필요하므로 모두 해주어야 함
dist = [[INF] * (N + 1) for i in range(N + 1)]


def dijkstra(start, d):
    pq = []
    d[start] = 0  # 시작 - 목적지 동일 시 시간 0

    for v in graph[start]:
        heapq.heappush(pq, [v[0], v[1]])  # pq에 시간, 목적지 삽입

    while pq:
        w, cur = heapq.heappop(pq)

        if d[cur] != INF:
            continue

        d[cur] = w  # INF가 아니면 거리 갱신

        for v in graph[cur]:
            if d[v[1]] == INF:
                heapq.heappush(pq, [w + v[0], v[1]])


for i in range(1, N + 1):
    dijkstra(i, dist[i])

result = [0]
for i in range(1, N + 1):
    # 출발지 - 목적지 - 출발지 (왕복)
    result.append(dist[i][X] + dist[X][i])

print(max(result))