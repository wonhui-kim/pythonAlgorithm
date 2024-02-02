import sys

# 지역 개수 n, 수색 범위 m, 길 개수 r
n, m, r = map(int, sys.stdin.readline().split())

# 구역 별 아이템 수
items = list(map(int, sys.stdin.readline().split()))

INF = int(10e9)
graph = [[INF for i in range(n)] for j in range(n)]
for i in range(r):
    a, b, l = map(int, sys.stdin.readline().split())

    graph[a - 1][b - 1] = l
    graph[b - 1][a - 1] = l


def floyd_warshall(arr):
    for k in range(len(arr)):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i == j:
                    arr[i][j] = 0

                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])


def gain_items(items, arr, scope):
    result = -1

    for i in range(len(arr)):
        total = 0
        for j in range(len(arr)):
            if arr[i][j] <= scope:
                total += items[j]

        result = max(result, total)

    return result


floyd_warshall(graph)
print(gain_items(items, graph, m))