import sys
import heapq

V = int(sys.stdin.readline())
graph = [[] for i in range(V + 1)]
for i in range(V):
    temp = list(map(int, sys.stdin.readline().split()))

    start = temp[0]
    end = temp.index(-1)

    if end > 1:
        for j in range(1, end, 2):
            graph[start].append([temp[j], temp[j + 1]])


def dijkstra(start):
    dist = [-1 for i in range(V + 1)]
    dist[start] = 0

    pq = []
    for v in graph[start]:
        n, d = v

        heapq.heappush(pq, [-d, n])  # 최대 힙 만들기

    while pq:
        d, n = heapq.heappop(pq)
        d *= -1  # 원래 값으로 복구

        if dist[n] != -1:  # 이미 갱신된 값이면
            continue

        dist[n] = d

        for v in graph[n]:
            if dist[v[0]] == -1:
                heapq.heappush(pq, [-1 * (d + v[1]), v[0]])

    return dist


# 임의의 노드로부터 가장 먼 거리의 노드는 트리의 양 끝점 중 하나
find_leaf = dijkstra(1)
leaf = 0
max_dist = -1
for i in range(len(find_leaf)):
    if find_leaf[i] > max_dist:
        max_dist = find_leaf[i]
        leaf = i

another_leaf = dijkstra(leaf)
print(max(another_leaf))