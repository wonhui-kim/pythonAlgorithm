import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [[] for i in range(n + 1)]

for i in range(n - 1):
    a, b, w = map(int, sys.stdin.readline().split())

    graph[a].append([w, b])
    graph[b].append([w, a])


def bfs(start):
    dist = [-1] * (n + 1)
    dist[start] = 0

    max_dist = 0
    node = start

    deq = deque()
    for v in graph[start]:
        deq.append(v)

    while deq:
        d, cur = deq.popleft()

        if dist[cur] != -1:
            continue

        dist[cur] = d
        if d > max_dist:
            max_dist = d
            node = cur

        for v in graph[cur]:
            if dist[v[1]] == -1:
                deq.append([d + v[0], v[1]])

    return node, dist


start_node, temp = bfs(1)
end_node, dist = bfs(start_node)
print(dist[end_node])