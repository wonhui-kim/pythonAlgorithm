import sys

V, E = map(int, sys.stdin.readline().split())

INF = int(10e9)
graph = [[INF for j in range(V)] for i in range(V)]
for i in range(E):
    a, b, c = map(int, sys.stdin.readline().split())

    graph[a - 1][b - 1] = c


def floyd_warshall(arr, num):
    for k in range(num):
        for i in range(num):
            for j in range(num):
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

    return arr


floyd_warshall(graph, V)

# 왕복 거리 최단거리 구하기
min_way = INF
for i in range(V):
    for j in range(i + 1, V):
        min_way = min(min_way, graph[i][j] + graph[j][i])

if min_way >= INF:
    print(-1)
else:
    print(min_way)
