import sys

n, k = map(int, sys.stdin.readline().split())

INF = int(10e9)
graph = [[INF for i in range(n + 1)] for j in range(n + 1)]

for i in range(k):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = -1
    graph[b][a] = 1


def floyd_warshall(arr, N):
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if arr[i][j] == INF: #명확하게 전후관계 알 수 있는 경우에만 갱신
                    if graph[i][k] == 1 and graph[k][j] == 1:
                        graph[i][j] = 1
                    elif graph[i][k] == -1 and graph[k][j] == -1:
                        graph[i][j] = -1


floyd_warshall(graph, n)

s = int(sys.stdin.readline())
for i in range(s):
    a, b = map(int, sys.stdin.readline().split())

    if graph[a][b] == INF:
        print(0)
    else:
        print(graph[a][b])