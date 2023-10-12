import sys

# 사람 수, 관계 수
N, K = map(int, sys.stdin.readline().split())

INF = int(10e9)
graph = [[INF for j in range(N + 1)] for i in range(N + 1)]

for i in range(K):
    A, B = map(int, sys.stdin.readline().split())
    graph[A][B] = 1
    graph[B][A] = 1


def floyd_warshall(arr, length):
    for k in range(1, length):
        for i in range(1, length):
            for j in range(1, length):
                if i == j:
                    arr[i][j] = 0

                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])


def find_max(arr, length):
    max_value = -1
    for i in range(1, length):
        for j in range(1, length):
            max_value = max(max_value, arr[i][j])

    return max_value


floyd_warshall(graph, N + 1)
if 6 >= find_max(graph, N + 1):
    print("Small World!")
else:
    print("Big World!")