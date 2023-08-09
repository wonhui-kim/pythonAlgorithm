import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
# 방문 가능 여부 - 1이면 불가
possible = list(map(int, sys.stdin.readline().split()))
possible[-1] = 0  # 마지막 노드는 목적지 노드이기 때문에 방문 가능으로 변경

graph = [[] for i in range(N)]  # 0부터 N-1까지
for i in range(M):
    a, b, t = map(int, sys.stdin.readline().split())
    graph[a].append([t, b])  # 가중치, 도착 노드 저장
    graph[b].append([t, a])  # 양방향

INF = int(10e9)
dist = [INF] * N


def dijkstra(start):
    pq = []
    dist[start] = 0

    for v in graph[start]:
        if possible[v[1]] == 0:  # 방문 가능한 노드만 넣음
            heapq.heappush(pq, [v[0], v[1]])

    while pq:
        w, cur = heapq.heappop(pq)

        if dist[cur] != INF:
            continue

        if possible[cur] == 0:  # 방문 가능한 노드일 때만
            dist[cur] = w

            for v in graph[cur]:
                if dist[v[1]] == INF:
                    heapq.heappush(pq, [w + v[0], v[1]])


dijkstra(0)  # start는 0번

if dist[N - 1] >= INF:
    print(-1)
else:
    print(dist[N - 1])