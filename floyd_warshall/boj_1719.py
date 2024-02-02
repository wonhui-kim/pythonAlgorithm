import sys

n, m = map(int, sys.stdin.readline().split())

INF = int(10e9)
graph = [[INF for i in range(n)] for j in range(n)]
result = [["-" for i in range(n)] for j in range(n)]

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())

    graph[a - 1][b - 1] = c
    graph[b - 1][a - 1] = c

    result[a - 1][b - 1] = str(b)
    result[b - 1][a - 1] = str(a)


def floyd_warshall(arr):
    for k in range(len(arr)):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i == j:
                    arr[i][j] = 0

                if arr[i][j] > (arr[i][k] + arr[k][j]):
                    arr[i][j] = arr[i][k] + arr[k][j]
                    result[i][j] = result[i][k]


def print_result(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end=' ')
        print()


floyd_warshall(graph)
print_result(result)