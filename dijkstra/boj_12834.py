import sys
import heapq

N, V, E = map(int, sys.stdin.readline().split())
A, B = map(int, sys.stdin.readline().split())
home = list(map(int, sys.stdin.readline().split()))

graph = [[] for i in range(V + 1)]
for i in range(E):
    a, b, l = map(int, sys.stdin.readline().split())

    graph[a].append([l, b])
    graph[b].append([l, a])

INF = int(10e9)


def dijkstra(start):
    dist = [INF for i in range(V + 1)]
    dist[start] = 0
    pq = []

    for v in graph[start]:
        heapq.heappush(pq, v)

    while pq:
        d, cur = heapq.heappop(pq)

        if dist[cur] != INF:
            continue

        dist[cur] = d

        for v in graph[cur]:
            if dist[v[1]] == INF:
                heapq.heappush(pq, [d + v[0], v[1]])

    return dist


def shortest_sum(arr, a, b):
    result = 0

    # 집-A + 집-B 거리 합 (반대로 a, b부터 각 사람들의 집까지의 거리를 합하면 답)
    distance_a = dijkstra(a)
    distance_b = dijkstra(b)

    for ar in arr:
        from_a = distance_a[ar]
        from_b = distance_b[ar]

        if from_a == INF:
            from_a = -1
        if from_b == INF:
            from_b = -1

        result += (from_a + from_b)

    return result


print(shortest_sum(home, A, B))