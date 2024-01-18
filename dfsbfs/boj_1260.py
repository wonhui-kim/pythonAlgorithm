import sys
from collections import deque


def dfs(start, v, matrix):
    v[start] = True  # 방문 처리
    print(start, end=' ')

    matrix[start].sort()

    for vertex in matrix[start]:
        if not v[vertex]:
            dfs(vertex, v, matrix)


def bfs(start, v, matrix):
    deq = deque()
    deq.append(start)
    v[start] = True

    while deq:
        cur = deq.popleft()
        print(cur, end=' ')

        for vertex in matrix[cur]:
            if not v[vertex]:
                deq.append(vertex)
                v[vertex] = True


N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for i in range(N + 1)]
visited = [False for i in range(N + 1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)

dfs(V, visited, graph)
print()
visited = [False for i in range(N + 1)]  # 방문 배열 초기화
bfs(V, visited, graph)