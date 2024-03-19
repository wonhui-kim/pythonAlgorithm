import sys

n, m = map(int, sys.stdin.readline().split())

INF = int(10e9)
graph = [[INF for i in range(n + 1)] for j in range(n + 1)]

for i in range(m):
    u, v, b = map(int, sys.stdin.readline().split())

    graph[u][v] = 0
    graph[v][u] = 1  # 교체 비용 추가

    if b == 1:  # 양방향길
        graph[v][u] = 0


def floyd_warshall(arr):
    for k in range(1, len(arr)):
        for i in range(1, len(arr)):
            for j in range(1, len(arr)):
                if i == j:
                    arr[i][j] = 0

                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

    return arr


graph = floyd_warshall(graph)

k = int(sys.stdin.readline())
for i in range(k):
    s, e = map(int, sys.stdin.readline().split())

    print(graph[s][e])