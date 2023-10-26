import sys
import itertools
from collections import deque
import copy

N, M = map(int, sys.stdin.readline().split())

graph = [[] for i in range(N + 1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)


def find_location(first, second, dist):
    deq = deque()
    deq.append(first)
    deq.append(second)

    dist[first] = 0
    dist[second] = 0

    while deq:
        cur = deq.popleft()

        for v in graph[cur]:
            if dist[v] == INF:
                dist[v] = min(dist[v], dist[cur] + 2)
                deq.append(v)

    result = sum(dist[1:N + 1])

    return result


# 조합으로 2개를 뽑은 후 최단거리 비교
INF = int(10e9)
dist_origin = [INF for i in range(N + 1)]
answer = INF
a, b = -1, -1
for i in itertools.combinations(range(1, N + 1), 2):
    d = copy.deepcopy(dist_origin)
    if answer > find_location(i[0], i[1], d):
        answer = find_location(i[0], i[1], d)
        a, b = i[0], i[1]

print(a, b, answer)