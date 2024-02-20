import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
graph = [[] for i in range(N + 1)]
for i in range(M):
    a, b, w = map(int, sys.stdin.readline().split())

    # 양방향
    graph[a].append([w, b])
    graph[b].append([w, a])

INF = int(10e9)
dist = [INF] * (N + 1)


def dijkstra(start):
    pq = []
    dist[start] = 0

    for v in graph[start]:
        heapq.heappush(pq, [v[0], v[1], start])  # 가중치, 끝점, 시작점

    recover = []
    while pq:
        d, cur, prev = heapq.heappop(pq)

        if dist[cur] != INF:
            continue

        dist[cur] = d
        recover.append([prev, cur])

        for v in graph[cur]:
            if dist[v[1]] == INF:
                heapq.heappush(pq, [d + v[0], v[1], cur])

    return recover


def print_result(arr):
    print(len(arr))

    for a in arr:
        print(a[0], a[1])
    print()


result = dijkstra(1)
print_result(result)